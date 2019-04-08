import time
import random
import requests

def get_json(url,page,lang_name):
    headers = {
        'Host': 'www.lagou.com',
       'Connection': 'keep-alive',
       'Content-Length': '23',
       'Origin': 'https://www.lagou.com',
       'X-Anit-Forge-Code': '0',
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
       'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
       'Accept': 'application/json, text/javascript, */*; q=0.01',
       'X-Requested-With': 'XMLHttpRequest',
       'X-Anit-Forge-Token': 'None',
       'Referer': 'https://www.lagou.com/jobs/list_python?city=%E6%B7%B1%E5%9C%B3&cl=false&fromSearch=true&labelWords=&suginput=',
       'Accept-Encoding': 'gzip, deflate, br',
       'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
       'cookie':"user_trace_token=20190409012203-585b5ec4-1ac2-4d27-b9dd-7bcd17438398; WEBTJ-ID=20190409012202-169fdf89d2e253-0b9f3874cbecf-e323069-2073600-169fdf89d2fbeb; _ga=GA1.2.788283279.1554744123; _gid=GA1.2.257614836.1554744123; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1554744123; LGSID=20190409012203-d3844b44-5a22-11e9-9d37-525400f775ce; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=sp0.baidu.com; PRE_SITE=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZNKw_0rwqB0FNkUs046lVT00000DFwAdC00000LYGo4f.THd_myIEIfK85yF9pywd0ZnquHuhPAndnWcsnj0kuhmsnsKd5RmsPbNjPYmsfHcYwRDdwWuaPbDYnYFafbNAnbR4nHNK0ADqI1YhUyPGujY1nWckPWfsPj04FMKzUvwGujYkP6K-5y9YIZK1rBtEILILQhk9uvqdQhPEUiq_TaqCIAd_QLKETv-Ypyq8Qh9YUysOIgwVgLPEIgFWuHdVgvPhgvPsI7qBmy-bINqsmvFY0APzm1YkPHc1%26tpl%3Dtpl_11534_19713_15764%26l%3D1511739714%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E3%252580%252591-%252520%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E5%2525AE%25259E%2525E6%252597%2525B6%2525E6%25259B%2525B4%2525E6%252596%2525B0%21%2526xp%253Did%28%252522m3221640409_canvas%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D40%26ie%3DUTF-8%26f%3D8%26tn%3Dbaidu%26wd%3Dlagou%26oq%3Dlagou%26rqlang%3Dcn; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fposition.html%3Futm_source%3Dm_cf_cpt_baidu_pcbt; LGUID=20190409012203-d3844ec2-5a22-11e9-9d37-525400f775ce; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22169fdf8c0a731c-01fd4baa070ca1-e323069-2073600-169fdf8c0a8b97%22%2C%22%24device_id%22%3A%22169fdf8c0a731c-01fd4baa070ca1-e323069-2073600-169fdf8c0a8b97%22%7D; sajssdk_2015_cross_new_user=1; LG_LOGIN_USER_ID=f69c62a255fbc8b627d57d52d13317d3a7c6235497fc558b; _putrc=9C422A4C9E48A1A4; JSESSIONID=ABAAABAABEEAAJA9C8884B3245E1A5EFFBE20398568D054; login=true; unick=%E9%82%B9%E7%81%B5%E5%BD%AC; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=31; gate_login_token=abdb5efec94f13dd33d0ffe5141ad17078ed630d2ba54f8b; index_location_city=%E6%B7%B1%E5%9C%B3; TG-TRACK-CODE=index_navigation; SEARCH_ID=c1942dba98ae4d2092a5c09a44b5af7f; X_HTTP_TOKEN=273612586aea0d7772344745518e0ec9d6cbf4bd7f; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1554744327; LGRID=20190409012527-4cd7d116-5a23-11e9-8cd6-5254005c3644"
    }
    proxies = {'http':"https://116.209.58.237"}

    data = {'first':'true','pn':page,'kd':lang_name}
    json = requests.post(url,data,headers=headers,proxies=proxies).json()
    print(json)

def main():
    lang_name = 'python'
    for i in ['广州', '深圳']:
        page = 1
        url = 'https://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionalResult=false'.format(i)
        while page<31:
            get_json(url,page,lang_name)
            page += 1
            time.sleep(random.randint(10, 20))

if __name__ == '__main__':
    main()