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

def insert_xiaoquinfo(xiaoquinfo_list):
    conn = pymysql.connect(host,user,passwd,dbname,charset='utf8' )
    cursor = conn.cursor()
    for item in xiaoquinfo_list:
        print(item)
        sql = "INSERT INTO xiaoquinfo (xiaoqu_name, xiaoqu_url, build_time, build_type, pm_price, pm_compnay, build_company, sum_buildings, sum_apartments, create_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, item)
    conn.commit()
    conn.close()

def read_file_inline():
    f = open("/var/log/xiaoqu.log","r")
    xiaoquinfo_list = []
    xiaoqu_strs = f.readlines()
    for xiaoqu_str in xiaoqu_strs:
        xiaoqu_list = xiaoqu_str.split("    ")
        xiaoqu_list[-1] = xiaoqu_list[-1].strip()
        xiaoquinfo_list.append(xiaoqu_list)
    return xiaoquinfo_list

xiaoquinfo_list = read_file_inline()
insert_xiaoquinfo(xiaoquinfo_list)
