import requests
import re
from bs4 import BeautifulSoup
import bs4
j = 0
soup = BeautifulSoup(open("lianjiaori.html", encoding='UTF-8'), "html.parser")
quxian = soup.find("div", class_ = re.compile('sub_nav section_sub_nav'))
print(type(quxian))
print(dir(quxian))
print(quxian.children)
for i in quxian.children:
    print(type(i))
    if (isinstance(i, bs4.element.Tag)):
        print(i)
print(quxian.a.string)
print(quxian.a.next_siblings)
print(quxian.a['title'])
print(quxian.a['href'])
#print(quxian[0])
#print(type(quxian[0]))
