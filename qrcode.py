# 爬取二维码的测试代码
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
        yield scrapy.Request(url="https://www.weixinqun.cn/city/guangzhou", callback=self.parse)
        
    def parse(self, response):
        selector = scrapy.Selector(response)
        title = selector.xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li/div[1]/a/@href").extract_first()
        for url in title:
            href = "https://www.weixinqun.cn" + url
            yield scrapy.Request(url=href,callback=self.wx_group)
            
            
    def wx_group(self,response):
        selector = scrapy.Selector(response)
        qrcode = selector.xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/img/@src').extract_first()
        master = selector.xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/p[1]/span').extract_first()
        res = DataItem
        for qr_code in qrcode:
            res['qr_code'] = "https://www.weixinqun.cn"+ qr_code
        for gp_master in master:
            res['gp_master'] = gp_master
        
        yield res
        #15:28:39 Request: (<GET https://www.weixinqun.cn.>) download failed reason: (404 Not Found) will retry later...