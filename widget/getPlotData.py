#!/usr/bin/python 693993
#-*- coding:utf-8 -*-
import linecache
import numpy as np
import matplotlib.pyplot as plt

def getPiePlot(totallist):
    plt.figure('Pie')
    rate=[]
    labels = []
    colors = []
    explode = []
    for x in totallist:
        if x == '0':
            labels.append('PASS')
            explode.append(0)
        else :
            labels.append(x)
            explode.append(0.05)
        rate.append(totallist[x])

    plt.pie(rate, explode=explode, labels=labels, autopct = '%.2f%%')
    plt.legend(rate)
    plt.title('Pie plot of yield', bbox={'facecolor':'0.8', 'pad':10})

def getScatterPlot(errlist):
    for x in errlist:
        #print(plt.style.available)
        plt.figure(x)
        plt.xlim(0, 30)
        plt.ylim(0, 40)
        plt.title('error' + x)

        xz = []
        yz = []
        for index, item in enumerate(errlist[x]):
            if index%2 == 0:
                xz.append(item)
            else :
                yz.append(item)
        print xz
        print yz
        plt.scatter(xz, yz)
        plt.xlabel('COL')
        plt.ylabel('ROW')
        plt.grid(True)
        #plt.style.use('seaborn-paper')

#totallist = {'24': 2, '0': 50, '29': 3, '25': 2, '23': 1}
#errlist = {'29': ['27', '26', '21', '22', '22', '23']}
def getPlot(totallist, errlist):
    getPiePlot(totallist)
    getScatterPlot(errlist)
    plt.show()
    plt.clf()
#getPlot(totallist, errlist)
#getPlotItem('/Grape/BigData/report_2016-01-05_08-59-22.txt')