#!/usr/bin/python
#-*- coding:utf-8 -*-
import os
import datetime
from generateReport import genr

def findDirs(path, kw):
    fileName = []
    for root, dirs, files in os.walk(path):
        for fn in dirs:
            if (fn.find(kw) != -1):
                fileName.append(root + fn + '/')
    return fileName

def findFiles(path, kw):
    #print kw
    fileName = []
    for root, dirs, files in os.walk(path):
        for fn in files:
            if (fn.find(kw) != -1 and len(fn) == 7):
                fileName.append(root + '/' +fn)
    return fileName

def dateLoop(sd, ed):  
    dateBuf = []
    begin = datetime.date(int(sd[:4]),int(sd[4:6]),int(sd[-2:])) 
    end = datetime.date(int(ed[:4]),int(ed[4:6]),int(ed[-2:])) 

    for i in range((end - begin).days+1):  
        day = begin + datetime.timedelta(days=i)  
        dateBuf.append(str(day).replace('-', '')) 
    return dateBuf

def csvName(rawBuf,):

    eerCode = rawBuf[1]
    eePath =  findDirs('/Grape/BigData/',rawBuf[0].upper())
    if len(rawBuf) == 3:
        cName = []
        csvFileName = rawBuf[2].upper() + '.csv'
        for x in eePath:
            nBuf = findFiles(x, csvFileName)
            if nBuf:
                cName = cName + nBuf
        genr(cName, eerCode)
    if len(rawBuf) == 4:
        cName = []
        for x in eePath:
            for y in dateLoop(rawBuf[2], rawBuf[3]):
                nBuf = findFiles(x + y, '.csv')
                if nBuf:
                    cName = cName + nBuf
        genr(cName, eerCode)

#csvName(['GT3x', '','G1b'])
#csvName(['GT3X', '','20151201', '20151230'])
