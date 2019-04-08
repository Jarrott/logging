import requests

url="https://test.trustdos.com/index/user/index.html"
cookie_dict = {
    "thinkphp_show_page_trace":"0|0",
    "PHPSESSID":"39l0m72b0pnklhumbh2r29r3t1",
    "token":"6ec6f1a2-5a63-448b-a8d7-8f45858ff482"
}

html = requests.get(url=url,cookies=cookie_dict).text
with open('D:/index.html','w',encoding='utf-8') as f:
    f.write(html)