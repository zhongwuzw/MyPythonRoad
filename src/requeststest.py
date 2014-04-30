import requests
import re
headers = {"X-Requested-With":"XMLHttpRequest"}
r = requests.get('http://bbs.byr.cn/board/Job/mode/6?_uid=guest',headers = headers)
r.encoding = 'GBK'
print r.text
