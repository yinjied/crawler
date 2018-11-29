from bs4 import BeautifulSoup
import datetime
import requests
import re
import pymysql
import bs4
host="139.198.19.54"
user = "crawler"
passwd = "crawler"
dbname = "test"

def log_write(info):
    try:
        f = open("/var/log/crawler.log","a")
        f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "    " + str(info))
        f.write("\n")

    finally:
        f.close()
def list_write(info):
    try:
        f = open("/var/log/xiaoquinfo.log","a")
        f.write(str(info))
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

def insert_xiaoquinfo(xiaoquinfo_list):
    conn = pymysql.connect(host,user,passwd,dbname,charset='utf8' )
    cursor = conn.cursor()
    for item in xiaoquinfo_list:
        print(item)
        sql = "INSERT INTO xiaoquinfo (xiaoqu_name, xiaoqu_url, build_time, build_type, pm_price, pm_compnay, build_company, sum_buildings, sum_apartments, create_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, item)
    conn.commit()
    conn.close()


xiaoqu_tuple = query_table_all("xiaoqu")
create_date = datetime.datetime.now().strftime('%Y-%m-%d')
xiaoquinfo_list = []
for xiaoqu in xiaoqu_tuple:
    xiaoqu_list = []
    xiaoqu_name = xiaoqu[1]
    xiaoqu_list.append(xiaoqu_name)
    xiaoqu_url = xiaoqu[2]
    xiaoqu_list.append(xiaoqu_url)
    xiaoqu_html = ""
    while True:
        xiaoqu_html = getHTMLText(xiaoqu_url)
        if isinstance(xiaoqu_html,int):
            print(xiaoqu_url)
            continue
        else:
            break
    xiaoqu_soup = BeautifulSoup(xiaoqu_html, "html.parser")
    xiaoqu_div = xiaoqu_soup.find("div", class_ = re.compile('xiaoquInfo'))
    if not (isinstance(xiaoqu_div, bs4.element.Tag)):
        log_write(xiaoqu_url)
        continue
    xiaoqu_price = xiaoqu_div.previous_sibling.find("span",class_ = re.compile("xiaoquUnitPrice")).string
    for label in xiaoqu_div:
        if label.span.string == "附近门店":
            break
        item = label.span.next_sibling.string
        xiaoqu_list.append(item)
    xiaoqu_list.append(xiaoqu_price)
    xiaoqu_list.append(create_date)
    print(xiaoqu_list)
    print(len(xiaoqu_list))
    if 11 != len(xiaoqu_list):
        log_write(xiaoqu_list)
        continue
    list_write(xiaoqu_list)
    #xiaoquinfo_list.append(xiaoqu_list)
#insert_xiaoquinfo(xiaoquinfo_list)
 

