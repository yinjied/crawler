from bs4 import BeautifulSoup
j=0
soup = BeautifulSoup(open("test.html", encoding='UTF-8'), "html.parser")
div = soup.children
type(div)
#print(div.div.contents[0])
#print(type(div.div.contents[0]))



