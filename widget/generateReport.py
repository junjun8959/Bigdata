#!/usr/bin/python
#-*- coding:utf-8 -*-

import transformQBJ
import getPlotData

errString ={
    '0':'PASS',
    '29':'phase_uniformity',
    '25':'uniformity',
    '16':'boardCalInfoCheckError',
    '57':'boardCalInfoCheckError',
    '22':'dcsig',
    '26':'phase',
    '33':'open_d1l',
    '34':'open_d1r',
    '30':'open_s1c',
    '31':'open_s1f',
    '64':'disabled_colCsigAvg_min',
    '65':'enabled_colCsigAvg_max'
}
def reportPath():
    from datetime import datetime
    curTime = datetime.now()
    path = '/Grape/BigData/report_' + str(curTime).replace(':', '-').replace(' ', '_').split('.')[0] + '.txt'
    print path
    return path
def genr(fileName, errCode = ''):
    totalList = {}
    errList = {}
    if errCode != '':
        print transformQBJ.strQ2B(errCode).split(',')
    for x in fileName:
        with open (x, 'rb') as cf:
            lines = cf.readlines()
            for line in lines:
                if line.find('err Code') == -1:
                    lineBuf = line.replace('\n', '').split(',')
                    print lineBuf
                    if lineBuf[4] in totalList:
                        totalList[lineBuf[4]] = totalList[lineBuf[4]] + 1  # 如果字典中有此err记录，计数加1
                    else :
                        totalList[lineBuf[4]] = 1                                      # 如果字典中没有直接记录1
                    if errCode !='':
                        ec = transformQBJ.strQ2B(errCode).split(',')
                        for e in ec:
                            if lineBuf[4] == e and lineBuf[2] != 'NA' and lineBuf[3] != 'NA':
                                if lineBuf[4] in errList:
                                    errList[lineBuf[4]] = errList[lineBuf[4]] + [lineBuf[2], lineBuf[3]]
                                else :
                                    errList[lineBuf[4]] = [lineBuf[2], lineBuf[3]]

            
    with open(reportPath(), 'wb') as rf:
        rf.write('------------------------- totalList -------------------------\n')
        rf.write('errCode\terrString\tQty\trate\n')
        total = 0.0
        for xx in totalList:
            total += int(totalList[xx])
        print total
        for x in totalList:
            if x in errString:
                rf.write(str(x)+ ' \t' + errString[x] + '\t' + str(totalList[x]) + '\t' + "%.2f%%"  %(totalList[x]/total*100)+ '\n')
            else :
                rf.write(str(x)+ ' \t' + 'No String' + '\t' + str(totalList[x]) + '\n')
        for y in errList:
            rf.write('------------------------- error' + str(y) + '-------------------------\n')
            rf.write('COL\tROW\n')
            #count = 0
            #for x in errList[y]:
            for index, item in enumerate(errList[y]):
                rf.write(str(item) + '\t')
                #count += 1
                if index % 2 != 0 :
                    rf.write('\n')
    rf.close()
    print 'write txt file success'
    getPlotData.getPlot(totalList, errList)
    
    