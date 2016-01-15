#-*- coding:utf-8 -*-
#File:statistical.py

import os
import csv
import linecache
import errArray
import errNone

global lineCount
lineCount = 0

PHASEUNIF = '[Uniformity (phase),'
#PUMINSPEC = -0.055
#PUMAXSPEC = 0.095

PHASE ='[Uniformity (amplitude),'
#PMINSPEC = -21.0
#PMAXSPEC = 16
#sd = {'OFFS_PHASE_UNIF_FINE_MIN':0,
#	  'OFFS_PHASE_UNIF_FINE_MAX':0,
#	  'OFFS_DCSIG_UNIF_FINE_MIN':0,
#	  'OFFS_DCSIG_UNIF_FINE_MAX':0 }

def printN(sn):
	pass

#errCode = {'29' : errArray.process,
#		   '25' : errArray.process, 
#		   None : errNone.process,
#		   }

#errFB = {'29' : (sd['OFFS_PHASE_UNIF_FINE_MIN'], sd['OFFS_PHASE_UNIF_FINE_MAX'], PHASEUNIF, '29'),
#		 '25' : (sd['OFFS_DCSIG_UNIF_FINE_MIN'], sd['OFFS_DCSIG_UNIF_FINE_MAX'], PHASE, '25'),
#		  None : 'errNum'
#		  }

LogPath = ["/Grape/LogsFolder/", "/vault/Grape/LogsFolder/"]
def findCSV(newData, specDict):

	sd = specDict
	LogFilePath = ''

	errCode = {'29' : errArray.process,
			   '25' : errArray.process, 
			   #'26' : errArray.process,
			   None : errNone.process,
			   }

	errFB = {'29' : (sd['OFFS_PHASE_UNIF_FINE_MIN'], sd['OFFS_PHASE_UNIF_FINE_MAX'], PHASEUNIF, '29'),
			 '25' : (sd['OFFS_DCSIG_UNIF_FINE_MIN'], sd['OFFS_DCSIG_UNIF_FINE_MAX'], PHASE, '25'),
			# '26' : (sd['OFFS_DCSIG_UNIF_FINE_MIN'], sd['OFFS_DCSIG_UNIF_FINE_MAX'], PHASE, '26'),
			  None : 'errNum'
			  }
			  
	errNum = newData[2]
	errInfo = errFB.get(errNum, errNum)
	for x in LogPath:
		if os.path.exists(x + newData[0] + '.log'):
			LogFilePath = x + newData[0] + '.log'
			print LogFilePath
			break
	if LogFilePath != '':
		errCode.get(errNum, errCode[None])(LogFilePath, newData[0], errInfo)

#findCSV('/Grape/Statistics/GrapeModule_FOS_3.3.0a6__1027.csv')
#newData = linecache.getline(CsvPath, lineNumber).split(',')
#print newData
#errNum = newData[2]
#errInfo = errFB.get(errNum, errNum)
#errCode.get(errNum, errCode[None])(LogPath + newData[0] + '.log', newData[0], errInfo)

