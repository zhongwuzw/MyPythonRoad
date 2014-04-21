# -*- coding: utf-8 -*-
import os
import re
opendir = u'E:/新建文本文档.txt'
f = open(opendir,'r')
opendestdir = u'E:/results.txt'
f1 = open(opendestdir,'w')
result = []
pattern = re.compile(r'#')
for line in f.readlines():
    line = line.strip()
#     if pattern.search(line):
    if line.find('#') != -1:
        line = line[:line.find('#')]
#         tempflag = line.find('#')
    if not len(line):
        continue
    result.append(line)
    
result.sort()
print result
f1.write('%s' %'\n'.join(result))
# str1 = u"E:/新建文本文档.txt"
# f = open(str1,'a').write("%s %s %s " %(u"字典",[u"数",u"组"],{u"字典" : 123}))

# str1 = u'D:/资料/'
# for object1 in os.listdir(str1) :
#     print object1
# str1 = u'H:/'
# for root,dirs,files in os.walk(str1):
#     print root,dirs
#     for strtemp in files:
#         if u'蝙蝠侠' in strtemp :
#             print strtemp