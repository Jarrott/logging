import os
import requests
from bs4 import BeautifulSoup as bs

result = []
def get_once_page(offset):
    url = "https://maoyan.com/board/4?offset=" + str(offset)
    response = requests.get(url).text
    content = bs(response,'lxml').find(name='dl',class_="board-wrapper")
    for data in content.find_all('dd'):
        rank = data.find('i').get_text()
        title = data.find('p',class_="name").get_text()
        actors = data.find('p',class_="star").get_text().strip()[3:]
        time = data.find('p',class_='releasetime').get_text().strip()[5:]
        score = data.find('p',class_="score").get_text()
        result_list = [int(rank),title,actors,time,float(score)]
        result.append(result_list)
    print(result)

def main():
    for i in range(10):
        get_once_page(i*10)

main()