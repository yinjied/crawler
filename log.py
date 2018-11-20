import os,sys,time
import datetime
import requests
import bs4
import re
from bs4 import BeautifulSoup

datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
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

demo = """<div class="page-box house-lst-page-box" comp-module="page" page-data='{"totalPage":2,"curPage":1}' page-url="/ershoufang/jiaodaokou/pg{page}/"></div>"""
soup = BeautifulSoup(demo, 'html.parser')
tag = soup.find("div")
print(tag)
print((tag['page-data']))
print(type(eval(tag['page-data'])['totalPage']))
