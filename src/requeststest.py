import requests
import re
from bs4 import BeautifulSoup

headers = {"X-Requested-With":"XMLHttpRequest"}
r = requests.get('http://bbs.byr.cn/board/Job/mode/6?_uid=guest',headers = headers)
r.encoding = 'GBK'
soup = BeautifulSoup(r.text)
tagset = soup.find_all('a',attrs = {'href':re.compile('^/article/Job/\d+$')})
templist = []
for tag in tagset:
    if tag.parent['class'][0] == 'title_9':
        templist.append(tag)
        print tag

