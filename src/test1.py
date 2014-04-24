# -*- coding: utf-8 -*-
import urllib
import chardet
rawdata = urllib.urlopen('http://www.qq.com').read()
tempcode = chardet.detect(rawdata)['encoding']
rawdata = rawdata.decode(tempcode,'ignore')
rawdata = rawdata.encode('utf-8')
# rawdata = unicode(rawdata,tempcode).encode('utf8')
print rawdata
# import os,sys
# print sys.argv