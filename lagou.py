import time
import random
import requests
from openpyxl import Workbook

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
       'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
    }
    data = {'first':'true','pn':page,'kd':lang_name}
    json = requests.post(url,data,headers=headers).json()
    print(json)
    # list_cont = json['content']['positionResult']['result']
    # info_list = []
    # for i in list_cont:
    #     info = []
    #     info.append(i.get('companyShortName', '无'))  # 公司名
    #     info.append(i.get('companyFullName', '无'))
    #     info.append(i.get('industryField', '无'))   # 行业领域
    #     info.append(i.get('companySize', '无'))  # 公司规模
    #     info.append(i.get('salary', '无'))   # 薪资
    #     info.append(i.get('city', '无'))
    #     info.append(i.get('education', '无'))    
    #     info_list.append(info)    #拼接重要信息
    
    # return info_list

def main():
    lang_name = 'python'
    wb = Workbook()
    for i in ['北京', '上海', '广州', '深圳', '杭州']:
        page = 1
        ws1 = wb.active
        ws1.title = lang_name
        url = 'https://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionalResult=false'.format(i)
        while page<31:
            get_json(url,page,lang_name)
            page += 1
            time.sleep(random.randint(10, 20))
            # for row in info:
            #     ws1.append(row)

    #wb.save('{}职位信息.xlsx'.format(lang_name))

if __name__ == '__main__':
    main()