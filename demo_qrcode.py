# Scrapy实例 Python语言 支持原生Scrapy开发
import scrapy
import time
import requests


class DataItem(scrapy.item.Item):
    title = scrapy.Field()
    qrcode = scrapy.Field()
    group_master = scrapy.Field()


class ShenjianSpider(scrapy.Spider):
    name = "shenjian"

    def start_requests(self):
        yield scrapy.Request(url="https://www.weixinqun.cn/city/hangzhou", callback=self.parse)

    def parse(self, response):
        selector = scrapy.Selector(response)
        title = selector.xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li/div/a/@href").extract()
        for url in title:
            _href = 'https://www.weixinqun.cn' + url
            yield scrapy.Request(url=_href,callback=self.weixin_group)

    def weixin_group(self,response):
        selector = scrapy.Selector(response)
        qrcode = selector.xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/img/@src').extract()
        group_master = selector.xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/p[1]/span').extract()
        res = DataItem()
        for qr_code in qrcode:
            res['qrcode'] = 'https://www.weixinqun.cn' + qr_code
        for gp_master in group_master:
            res['group_master'] = gp_master
        yield res
#         res = DataItem()
#         res['title'] = title
#         yield res
