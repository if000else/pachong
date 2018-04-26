
###爬取页数
PAGE_NUMS = 1
#程序爬取完当天数据的一个休眠时间
SLEEP_TIME=60*60*12

#当爬取频率过高网站被封时的休眠时间
ERROR_SLEEP_TIME = 60*60*2
#URL
BASE_URL = 'http://dj.evideocloud.com/gf/pc/web/video/getListByCategory'
HOME_PAGE = 'http://dj.evideocloud.com'

import requests
from bs4 import BeautifulSoup
import json


def browser(url,data=None):

    response = requests.get(url=url,data=data)
    return response.text

def parse(html):
    data = {}
    soup = BeautifulSoup(html,'lxml')
    #获取法院名称
    for item in soup.select('.name'):
        k1,v1 = item.find('h3').get_text().strip().split('：')
        data[k1] = v1
    #获取案情简介
    for item in soup.select('.pro'):
        k2 = item.find('h3').get_text()
        v2 = item.find('p').get_text()
        data[k2] = v2
    #获取庭审信息
    for item in soup.select('.casedetile'):
        #庭审信息
        k3 = item.find('h3').get_text()
        v3 = {}
        #基本信息，审判组织成员，当事人
        for item1 in item.select('.base h4'):
            h4_text = item1.get_text()
            value_dic = {}
            #基本信息
            if h4_text == '基本信息':
                base_info = item.select('.basebox')[0]
                title = base_info.select('.title')
                cont = base_info.select('.cont')
                for i in range(4):
                    k = title[i].get_text().strip()
                    v = cont[i].get_text().strip()
                    value_dic[k] = v
                v3[h4_text] = value_dic

            if h4_text == '审判组织成员':
                group_info = item.select('.basebox')[1]
                cont = group_info.select('.cont')[0]
                v3[h4_text] = cont.get_text().strip()
            if h4_text == '当事人':
                party = item.select('.basebox')[2]
                cont = party.select('.cont')
                # for c in cont:
                #     k,v = c.get_text().strip().split('：')
                #     value_dic[k] = v
                cont = party.select('.cont')[0]
                v3[h4_text] = cont.get_text().strip()
                v3[h4_text] = value_dic
        data[k3] = v3
    return data

def save(dada):
    with open('data.txt','a',encoding='utf-8') as f:
        dada = str(dada)
        f.write(dada)

def main():
    print('start sending url request...')
    head = {
        'page': None,
        'categoryId': 0,
        'tenantId': 9,
    }
    href_list = []
    for i in range(1,PAGE_NUMS + 1):
        print('get data of page[%s]:'%i)
        head['page'] = i
        html_page = requests.get(BASE_URL,head).text
        soup = BeautifulSoup(html_page,'lxml')
        if soup:
            # error page
            pass

        for item in soup.select('.pic'):
            dest_url = "%s%s" % (HOME_PAGE, item['href'])
            href_list.append(dest_url)
    print(href_list)
    for href in href_list:
        detail_page = browser(href)
        data = parse(detail_page)
        save(data)

if __name__ == '__main__':
    main()