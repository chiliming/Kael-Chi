# -*- coding: utf-8 -*-
'''
Created on Dec 2, 2015

@author: kael.Chi
'''

import TxtFileOperate
import httplib2
from bs4 import BeautifulSoup
import re
import DatumHand

if __name__ == '__main__':
    url_file_name = 'url.txt'
    url_file_mode = 'r'
    url_file_code = 'utf-8'
    h = httplib2.Http(".cache")
    board_url = []
    base_url = 'http://www.zgqpw.com.cn/Tour/'

    pass

url_hand = TxtFileOperate.TxtFileOperate()
url_temp = url_hand.HandleInputFile(url_file_name, url_file_mode, url_file_code)


for i in range(len(url_temp)):
    board_url = []
    resp, content = h.request(url_temp[i].strip(), "GET")
    soup = BeautifulSoup(content, "html.parser")
    for item in soup.find_all('a', text=re.compile("[0-9][0-9]?"),  href=re.compile("^Board")):
        board_url.append(item)
    for item in board_url:
        #print item['href']
        resp, content = h.request(base_url + item['href'], "GET")
        Hand = DatumHand.DatumHand()
        Hand.HandleDatumHand(content)
        Hand.PrintAllAttr()
        for item in soup.find_all('td', class_='hand'):
            print item.text
        print 'finish hand'
    print 'finish %d url'%(i+1)


