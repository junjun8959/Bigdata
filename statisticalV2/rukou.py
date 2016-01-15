#-*- coding:utf-8 -*-
#File:err29.py

import os
import time
import statistical
import linecache

realTime = time.time()
print realTime
sd = {}
# 生成SPCE字典
def spec(path):

	title = linecache.getline(path, 2).split(',')
	upper = linecache.getline(path, 3).split(',')
	lower = linecache.getline(path, 4).split(',')
	
	for index, item in enumerate(title):
		#print index, iterm
		if item[0:5] == 'OFFS_' or item[:6] == 'SHORT_':
			if item.find('MAX') != -1:
				sd[item] = upper[index]
			if item.find('MIN') != -1:
				sd[item] = lower[index]
csvTemp = ''

# 查找所有Grope CSV数据
def fun(path):
	fileName = []
	for root, dirs, files in os.walk(path):
		for fn in files:
			if (fn[0:11] == 'GrapeModule' and fn[-4:] == '.csv'):
				fileName.append(root + fn)
	return fileName
# 循环检测文件更新，读取最后一行数据
while 1:
	csvpath = ['/Grape/Statistics/','/vault/Grape/Statistics/']
	for x in csvpath:
		fileName = fun(x)
		for csv in fileName:
			if realTime < os.path.getmtime(csv):
				if csv != csvTemp:
					spec(csv)
					csvTemp = csv

				with open(csv, 'rb') as fh:  
				    first = next(fh)  
				    offs = -100  
				    while True:  
				        fh.seek(offs, 2)  
				        lines = fh.readlines()  
				        if len(lines)>1:  
				            last = lines[-1]  
				            break  
				        offs *= 2
				    # 传送前CSV前4个数据和字典   
				    statistical.findCSV(last.split(',')[0:4], sd)
				fh.close()
				realTime = os.path.getmtime(csv)
	time.sleep(10)
