from bs4 import BeautifulSoup
test = """<p>aaa<b>bbb</b></p>"""
test1 = """<p>
aaa
<b>
bbb
</b>
</p>"""

testsoup = BeautifulSoup(test, 'html.parser')
pretty = BeautifulSoup(test1, 'html.parser')
print(testsoup.p.contents)
print(pretty.p.contents)
