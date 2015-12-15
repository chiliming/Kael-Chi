'''
Created on Dec 15, 2015

@author: kael.Chi
'''
from TxtFileOperate import TxtFileOperate
import httplib2
from bs4 import BeautifulSoup
import re

if __name__ == '__main__':
    basedir = 'http://www.zgqpw.com.cn/Tour/'
    initdir = 'http://www.zgqpw.com.cn/Tour/TourYearPlan.aspx'
    h = httplib2.Http(".chache")
    output_filename = 'url'
    output_filemode = 'w'
    output_filecode = 'utf-8'
    toururl = []
    sectionuru = []
    sectionurl = []
    pass 


resp, content = h.request(initdir, "GET")
soup = BeautifulSoup(content, "html.parser")
for item in soup.find_all('a', href=re.compile("^TourIndex")):
    toururl.append(item['href'])
sectioncount = 1
for item_1 in toururl:
    item_1 = item_1.replace('Index', 'ResultText')
    item_1 = basedir + item_1
    print item_1
    resp_1, content_1 = h.request(item_1, "GET")
    soup_1 = BeautifulSoup(content_1, "html.parser")
    roundcount = 1
    for item_2 in soup_1.find_all('a', href=re.compile("^RoundResult")):
        a = item_2["href"]
        a = basedir + a
        sectionurl.append(a)
        print 'finish round %d'%roundcount
        roundcount += 1
    print 'finish section %d'%sectioncount
    sectioncount += 1

for item in sectionurl:
    item = item + '\n'
    print item

fhand = TxtFileOperate()
path = fhand.GetExtFilePath(output_filename)
fhand.OpenChFile(path, output_filemode, output_filecode)
for item in sectionurl:
    item = item + '\n'
    fhand.AppendLineToTxtFile(item)
fhand.CloseFile()




    
    