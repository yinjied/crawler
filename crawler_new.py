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

#api for log write
def log_write(info):
    try:
        f = open("/var/log/crawler.log","a")
        f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "    " + str(info))
        f.write("\n")

    finally:
        f.close()
#api for get html
def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url, headers = kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return r.status_code

#get the district info from tag
def formdistrict_list(tag):
    districts_dict = {}
    districts_list = []
    for item in tag:
        if (isinstance(item, bs4.element.Tag)):
            districts_dict[item.string] = 'https://'+ 'bj.lianjia.com' + item['href']
    districts_dict.pop('燕郊')
    districts_dict.pop('香河')
    for district in districts_dict:
        districts_list.append([district,districts_dict[district]])
    return districts_list

#insert the district and url to mysql
def insert_district(district_list):
    if (len(district_list) == 0):
        return 1
    conn = pymysql.connect(host,user,passwd,dbname,charset='utf8' )
    cursor = conn.cursor()
    for item in district_list:
        sql = "INSERT INTO district (district, district_url) VALUES (%s, %s)"
        cursor.execute(sql, (item[0], item[1]))
    conn.commit()
    conn.close()
    return 0

def query_table_all(table_name):
    conn = pymysql.connect(host,user,passwd,dbname,charset='utf8' )
    cursor = conn.cursor()
    #sql = "select * from %s"%table_name + " where district_url=%s and district=%s"
    sql = "select * from %s"%table_name
    #sql = "select * from district where district_url like %s"
    cursor.execute(sql)
    #cursor.execute(sql,("https://bj.lianjia.com/ershoufang/dongcheng/","东城"))
    ret = cursor.fetchall()
    return ret

def formstreet_list(tag, district):
    streets_list = []
    for item in tag:
        if (isinstance(item, bs4.element.Tag) and item.name == 'a'):
            street_url = 'https://'+ 'bj.lianjia.com' + item['href']
            streets_list.append([district,item.string,street_url])
    return streets_list

def formapartment_list(tag, page_url):
    apartment_list = []
    for item in tag:
        if item['class']==['clear', 'LOGCLICKDATA']:
            title_tag = item.find("div", class_ = re.compile('title'))
            address_tag = item.find("div", class_ = re.compile('address'))
            flood_tag = item.find("div", class_ = re.compile('flood'))
            followinfo_tag = item.find("div", class_ = re.compile('followInfo'))
            apartment_name = title_tag.a.string
            apartment_url = title_tag.a['href']

            xiaoqu_name = address_tag.div.a.string
            xiaoqu_url = address_tag.div.a['href']
            desc = ''
            for info in address_tag.strings:
                desc = desc + info
            for info in flood_tag.strings:
                desc = desc + info
            for info in followinfo_tag.strings:
                desc = desc + info

            priceInfo_tag = followinfo_tag.find("div", class_ = re.compile('priceInfo'))
            total_price = priceInfo_tag.div.span.string
            unit_price = priceInfo_tag.div.next_sibling.span.string
            '''
            print(total_price)
            print(unit_price)
            print('**************')
            print(apartment_name)
            print(apartment_url)
            print(xiaoqu_name)
            print(xiaoqu_url)
            print(desc)
            '''
            apartment_list.append([page_url,apartment_name,apartment_url,xiaoqu_name,xiaoqu_url,desc,total_price,unit_price])
        else:
            pass
    return apartment_list

def insert_street(street_list):
    if (len(street_list) == 0):
        return 1
    conn = pymysql.connect(host,user,passwd,dbname,charset='utf8' )
    cursor = conn.cursor()
    for item in street_list:
        sql = "INSERT INTO street (district, street, street_url) VALUES (%s, %s, %s)"
        cursor.execute(sql, (item[0], item[1], item[2]))
    conn.commit()
    conn.close()
    return 0

def insert_page(page_list):
    if (len(page_list) == 0):
        return 1
    conn = pymysql.connect(host,user,passwd,dbname,charset='utf8' )
    cursor = conn.cursor()
    for item in page_list:
        sql = "INSERT INTO page (street, page, page_url) VALUES (%s, %s, %s)"
        cursor.execute(sql, (item[0], item[1], item[2]))
    conn.commit()
    conn.close()
    return 0

def insert_apartment(apartment_list):
    if (len(apartment_list) == 0):
        return 1
    conn = pymysql.connect(host,user,passwd,dbname,charset='utf8' )
    cursor = conn.cursor()
    for item in apartment_list:
        sql = "INSERT INTO apartment (page_url, apartment_name, apartment_url, xiaoqu_name, xiaoqu_url, info, total_price, unit_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]))
    conn.commit()
    conn.close()
    return 0




if __name__ == "__main__":
    '''
    servername = 'bj.lianjia.com'
    url = 'https://' + servername + '/ershoufang/'
    demo = getHTMLText(url)
    soup = BeautifulSoup(demo, 'html.parser')
    districts_tag = soup.find("div", class_ = re.compile('sub_nav section_sub_nav'))
    districts_list = formdistrict_list(districts_tag)
    ret = insert_district(districts_list)
    
    district_tuple = query_table_all('district')
    for item in district_tuple:
        district_url = item[2]
        district_html = getHTMLText(district_url)
        district_soup = BeautifulSoup(district_html, 'html.parser')
        streets_tag = district_soup.find("div", class_ = re.compile('sub_sub_nav section_sub_sub_nav'))
        streets_list = formstreet_list(streets_tag, item[1])
        ret = insert_street(streets_list)
    
    street_tuple = query_table_all('street')
    page_list = []
    judge_list = []
    for item in street_tuple:
        street_url = item[3]
        street_name = item[2]
        street_html = getHTMLText(street_url)
        print(street_url)
        if isinstance(street_html,str):
            pass
        else:
            judge_list.append([street_name,street_url])
            print('judge_list:')
            print(street_url)
            continue

        street_soup = BeautifulSoup(street_html, 'html.parser')
        page_tag = street_soup.find("div", class_ = re.compile('page-box house-lst-page-box'))
        if page_tag is None:
            continue
        page_count = eval(page_tag['page-data'])['totalPage']
        for page in range(page_count):
            page_url = street_url + "pg" + str(page+1) + "/"
            page_list.append([street_name,str(page),page_url])
        print('***************************************************************************')
    print('last')
    print(len(page_list))
    ret = insert_page(page_list)
    print(ret)
    print(judge_list)
    '''
    page_tuple = query_table_all('page')

    for item in page_tuple:
        page_url = item[3]
        page_html = ''
        while True:
            page_html = getHTMLText(page_url)
            if isinstance(page_html,int):
                print(page_url)
                continue
            else:
                break
        page_soup = BeautifulSoup(page_html, 'html.parser')
        page_tag = page_soup.find("ul", class_ = re.compile('sellListContent'))
        if not (isinstance(page_tag, bs4.element.Tag)):
            log_write(page_url)
            print('write the url to var log')
            continue
        apartment_list = formapartment_list(page_tag, page_url)
        print(apartment_list[0])
        print(len(apartment_list))
        ret = insert_apartment(apartment_list)
        print(ret)
        print('*******************************************************')

