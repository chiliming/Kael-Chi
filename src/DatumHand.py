# -*- coding: utf-8 -*-
'''
Created on Nov 11, 2015

@author: kael.Chi
'''
from bs4 import BeautifulSoup
import re

class DatumHand():
    
    def __ini__(self):
        self.TourName = ''
        self.SectionName = ''
        self.Round = ''
        self.BoardNum = 0
        self.HandDict = dict()
        self.Datum = 0
        
    def HandleDatumHand(self, content):
        soup = BeautifulSoup(content, "html.parser")
        self.TourName = soup.find('span', id="lTourname").text
        self.SectionName = soup.find('span', id="lSectionName").text
        self.Round = soup.find('span', id = 'lRound').text
        self.BoardNum = int(soup.find('span', id="lBoardNo").text)
        #Find datum text and transfer to int.
        DatumText = soup.find('span', id="lDatum").text
        DatumList = ''.join(re.findall('[0-9]', DatumText))
        self.Datum = int(DatumList)
        
        
    def PrintAllAttr(self):
        print self.TourName 
        print self.SectionName 
        print self.Round 
        print self.BoardNum 
        #print self.HandDict 
        print self.Datum 