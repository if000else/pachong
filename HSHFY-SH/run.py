
###爬取页数
PAGE_NUMS = 1
#程序爬取完当天数据的一个休眠时间
SLEEP_TIME=60*60*12

#当爬取频率过高网站被封时的休眠时间
ERROR_SLEEP_TIME = 60*60*2
#URL
BASE_URL = 'http://dj.evideocloud.com/gf/pc/web/video/getListByCategory'

import requests
from bs4 import BeautifulSoup
import json


def browser(url,data=None):

    response = requests.get(url=url,data=data)
    return response.text

def parse(data):
    return

def save(data):
    pass

def main():
    print('start getting data...')
    head = {
        'page_num': None,
        'categoryId': 0,
        'tenantId': 9,
    }
    href_list = []
    for i in range(1,PAGE_NUMS + 1):
        print('get page [%s]:'%i)
        head['page_num'] = i
        html_page = browser(BASE_URL,data=head)

        soup = BeautifulSoup(html_page,'lxml')
        if soup:
            # error page
            pass
        ul = soup.find('ul',attrs={'class':"case"})
        for li in ul.find_all('li'):
            href_list.append(li.get('href'))
        print('get date of href_list,num:',len(href_list))
    for href in href_list:
        detail_page = browser(href)
        data = parse(detail_page)
        save(data)





if __name__ == '__main__':
    main()