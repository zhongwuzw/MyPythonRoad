# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup

headers = {"X-Requested-With":"XMLHttpRequest"}
r = requests.get('http://bbs.byr.cn/board/Job/mode/6?_uid=guest',headers = headers)
print r.encoding
# r.encoding = 'GBK'
# soup = BeautifulSoup(r.text)
# print soup
temp = u'中国a'
li = [temp[i] for i in range(len(temp)) if temp[i] >= u'\u4e00' and temp[i] <= u'\u9fff']
for i in li:
    print i
# tagset = soup.find_all('a',attrs = {'href':re.compile('^/article/Job/\d+$')})
# templist = []
# for tag in tagset:
#     if tag.parent['class'][0] == 'title_9':
#         templist.append(tag)
#         print tag

