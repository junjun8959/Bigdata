#-*- coding:utf-8 -*-
#File:err0.py
import writeData

def process(sn, barcode, errInfo):
	writeData.writeCSV(barcode + ',' + barcode[-3:] + ',' + 'NA' + ',' + 'NA' + ',' + errInfo + ',' + 'NA', barcode)
	print barcode + ',' + barcode[-3:] + ',' + 'NA' + ',' + 'NA' + ',' + 'NA' + ',' + errInfo + ':' + barcode
	