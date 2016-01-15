#/usr/bin/pytnon
#-*- coding:utf-8 -*-
#File:writeData.py

import os
import sys
import csv
import linecache
import time
# 记录数据
def recordCSV(fileName, record):
	print fileName
	with open(fileName, 'a') as bdfile:
		bdfile.write(record+'\n')
		bdfile.close

#删除一行
def removeLine(filename, lineno):

    fro = open(filename, "rb")
    lineno

    current_line = 0
    while current_line < lineno:
        fro.readline()
        current_line += 1

    seekpoint = fro.tell()
    seekpoint

    frw = open(filename, "r+b")
    frw.seek(seekpoint, 0)

    # read the line we want to discard
    fro.readline()

    # now move the rest of the lines in the file 
    # one line back 
    chars = fro.readline()
    while chars:
        frw.writelines(chars)
        chars = fro.readline()

    fro.close()
    frw.truncate()
    frw.close()

def removeRepeat(fileName, barcode, record):
	f = open(fileName, 'rw')
	lineNumber = 0
	#print record
	reLine = []
	writeWithout = True
	#查找重复记录
	for row in f:

		if row.find(barcode) != -1:
			if (record.split(',')[4] == '0' or row.split(',')[4].replace('\n', '') != '0' ):
				reLine.append(lineNumber)
			else :
				writeWithout = False
		lineNumber += 1
	f.close()
	#删除重复记录
	if len(reLine) != 0:
		for rl in sorted(reLine, reverse=True):
			removeLine(fileName, rl)
		recordCSV(fileName, record)
	#无重复记录时直接记录
	elif writeWithout:
		recordCSV(fileName, record)

	

def writeCSV(record, barcode):
	# 获得当前日期作为4阶路径
	from datetime import datetime
	curTime = datetime.now()
	datenow = str(curTime).split(' ')[0].replace('-', '')
	# 组合数据存放路径
	dataPath = '/Grape/BigData/' + barcode[0:3] + barcode[11:15] + '/' + datenow + '/'
	# 组合文件名
	csvName = dataPath + barcode[-3:] + '.csv'

	# 检测路径是否存在，如不在创建一个
	if not os.path.exists(dataPath):
		os.makedirs(dataPath)
	# 检测文件是否存在，如不在生成一个并写入title
	if not os.path.exists(dataPath+ barcode[-3:] + '.csv'):
		with open(csvName, 'w') as f:
			f.write('Barcode,Config,Col Location, Row Location, err Code,Value\n')
			f.close
	# 调用函数查找并删除重复的记录并记录新数据
	removeRepeat(csvName, barcode, record)

#writeCSV('D2C54240NVMGT3X2SG1B,G1B,NA,NA,0', 'D2C54240NVMGT3X2SG1B')