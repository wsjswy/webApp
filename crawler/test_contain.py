#coding=utf-8

import  copy
import  xlrd
from crawler.URL import  URL
from  contain import  is_similar_url

urlList=[]

result=[]

#读取excle文件

excelList = xlrd.open_workbook("/Users/wsjswy/Downloads/111.xlsx")

print excelList.nsheets

sh = excelList.sheet_by_index(0)

print sh.nrows

cell = sh.cell_value(100, 0)

i = 1
urlInfo = sh.cell_value(0,0)
result.append(urlInfo)

print 'first:  ' + urlInfo
while i < sh.nrows:

    a = sh.cell_value(i, 0)
    i += 1
    flag = True
    for b in result:
        #print b
        if is_similar_url(a, b):
            flag = False
    if flag:
        print 'newurl： '  + str(a)
        result.append(a)



print len(result) + 1