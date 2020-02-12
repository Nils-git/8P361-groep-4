# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:51:22 2020

@author: 20160824
"""

import csv
import matplotlib.pyplot as plt

def readcsv(read_filename):
    with open(read_filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        walltime = []
        step= []
        value = []
        for row in readCSV:
            time = row[0]
            stp= row[1]
            val = row[2]
            walltime.append(time)
            step.append(stp)
            value.append(val)
    #step correction
    step.pop()
    step.append(10)
    return walltime,step,value
    
def files(amount_of_files):
    value=[]
    colours=['r','g','b','k','y','m','c']
    for i in range(amount_of_files):
        num=str(i+1)
        file=input("Enter filename of CSV file "+num+ " with extension: ")
        t,s,v= readcsv(file)
        t=t[1:]
        s=s[1:]
        v=v[1:]
        #Rounding necessary because of a bug in plotting
        for val in range(len(v)):
            v[val]=round(float(v[val]),10)
        plt.plot(s,v,colours[i])
        value.append(v)
    plt.show()

##Fill in number of files to be analysed (maximum of 7)
number=2
files(number)
##