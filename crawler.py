import requests
import bs4
import re
import datetime
from bs4 import BeautifulSoup
import pymysql
host="139.198.19.54"
user = "crawler"
passwd = "crawler"
dbname = "test"
def log_write(info):
    try:
        f = open("D:\crawler\log","a")
        f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "    " + str(info))
        f.write("\n")

    finally:
        f.close()

def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url, headers = kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return r.status_code

def formdistricts(tag):
    districts_dict = {}
    for item in tag:
        if (isinstance(item, bs4.element.Tag)):
            districts_dict[item.string] = 'https://'+ 'bj.lianjia.com' + item['href']
    districts_dict.pop('燕郊')
    districts_dict.pop('香河')
    return districts_dict

def formstreetdicts(tag):
    streets_dict = {}
    for item in tag:
        if (isinstance(item, bs4.element.Tag) and item.name == 'a'):
            streets_dict[item.string] = item['href']
    return streets_dict

def formapartmentdicts(tag):
    apartments_dict = {}
    for item in tag:
        log_write('this is apartment')
        log_write(item)
        log_write(type(item))
        log_write(item['class'])
        if (isinstance(item, bs4.element.Tag) and item['class'] == ['clear', 'LOGCLICKDATA']):
            log_write("the process begin")
            datahousecode = item.a['href'].split('/')[-1].split('.')[0]
            url = item.a['href']
            title = item.find('div', {'class':'title'})
            desc = title.a.string
            apartments_dict[datahousecode] = [url, desc]
            log_write('this is apartments_dict')
            log_write(apartments_dict)
    return apartments_dict
def insert_district(district_dict):
    if (len(district_dict) == 0):
        return 1
    conn = pymysql.connect(host,user,passwd,dbname,charset='utf8' )
    cursor = conn.cursor()
    for item in district_dict:
        sql = "INSERT INTO district (district, district_url) VALUES (%s, %s)"
        cursor.execute(sql, (item, district_dict[item]))
    conn.commit()
    conn.close()
    return 0


        
if __name__ == "__main__":
    servername = 'bj.lianjia.com'
    #创建一个关于区县和url关系的字典
    url = 'https://' + servername + '/ershoufang/'
    demo = getHTMLText(url)
    soup = BeautifulSoup(demo, 'html.parser')
    districts_tag = soup.find("div", class_ = re.compile('sub_nav section_sub_nav'))
    districts_dict = formdistricts(districts_tag)
    ret = insert_district(districts_dict)
'''
    #print(districts_dict)

    #创建一个多层字典最外层是区县，区县内部的字典是街道和url的字典
    streets_dict = {}
    for district in districts_dict:
        district_url = 'https://' + servername + districts_dict[district]
        district_str = getHTMLText(district_url)
        district_soup = BeautifulSoup(district_str, 'html.parser')
        streets_tag = district_soup.find("div", class_ = re.compile('sub_sub_nav section_sub_sub_nav'))
        streets_dict[district] = formstreetdicts(streets_tag)
    #创建一个关于房子的字典，字典内容为街道：房子：url pagecount
    apartments_list = []
    for district in streets_dict:
        for street in streets_dict[district]:
            street_url = 'https://' + servername + streets_dict[district][street]
            street_str = getHTMLText(street_url)
            street_soup = BeautifulSoup(street_str, 'html.parser')
            page_tag = street_soup.find("div", class_ = re.compile('page-box house-lst-page-box'))
            page_count = eval(page_tag['page-data'])['totalPage']
            log_write('this is page_tag')
            log_write(page_tag)

            for page in range(page_count):
                log_write('this is page')
                log_write(page)
                page_url = street_url + 'pg' + str(page + 1)
                log_write('this is page_url')
                log_write(page_url)
                page_str = getHTMLText(page_url)
                page_soup = BeautifulSoup(page_str, 'html.parser')
                apartment_tag = page_soup.find("ul", class_ = re.compile('sellListContent'))
                log_write('this is apartment_tag')
                log_write(apartment_tag)
                apartments_list.append(formapartmentdicts(apartment_tag))
                print(apartments_list)
'''
