#-*- coding:utf-8 -*-
#File:errArray.py

import linecache
import writeData

def findLocation(sn, lineNum, Value, barcode, errNum):
	rowTotal = int(linecache.getline(sn, lineNum+1).replace(' ', '').split('\t')[0].replace('row', '').replace('[', '').replace(']', ''))
	for addRow in xrange(1,rowTotal+2):
		strRow = linecache.getline(sn, lineNum+addRow)
		#print strRow
		if strRow.find(str(Value)) != -1:
			#print strRow.replace(' ','').split('\t')
			colLocation = strRow.replace(' ','').replace('\n', '').split('\t').index(str(Value))-1
			rowLocation = rowTotal+1 - addRow
			logData = barcode + ',' + barcode[-3:] +',' + str(colLocation) + ',' + str(rowLocation) + ',' + errNum + ',' + str(Value)
			#print logData
			print logData
			writeData.writeCSV(logData, barcode)
			break
def process(sn, barcode, errInfo):
	MINSPEC = errInfo[0]
	MAXSPEC = errInfo[1]
	#print errInfo
	findInfo = errInfo[2]
	errNum = errInfo[3]
	lineCount = 0
	#print "errArray"
	# 打开logFile，查找不良项的值和坐标
	try:
		with open(sn) as logFile:
#		print "logfile is ok"
		#while 1:
			lines = logFile.readlines()
			#print lines
			#if not lines:
			#	break
			for line in lines:
				lineCount += 1
			#print lineCount  #共有多少行
			for lineNum in xrange(1,lineCount):
				#print lineNum
				strBuffer = linecache.getline(sn, lineCount-lineNum)
				#print strBuffer	#行内容
				if strBuffer.startswith(findInfo):
					minValue = float(strBuffer.split(',')[2].split('=')[1].replace(' ', ''))
					maxValue = float(strBuffer.split(',')[4].split('=')[1].replace(' ', '')
						.replace(']', '').replace('\n', ''))
					if maxValue > MAXSPEC:
						print maxValue, MAXSPEC
						findLocation(sn, lineCount-lineNum, maxValue, barcode, errNum)
					elif minValue < MINSPEC:
						print minValue, MINSPEC
						findLocation(sn, lineCount-lineNum, minValue, barcode, errNum)
					break
		logFile.close()
	except Exception, e:
		writeData.writeCSV(barcode + ',' + barcode[-3:] + ',' + 'NA' + ',' + 'NA' + ',' + errNum + ',' + 'NA', barcode)
		print e
