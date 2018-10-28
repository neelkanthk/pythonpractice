#!/usr/bin/python

# This script read a text file and saves its bytes into another file
import os
from time import strftime
stamp = strftime("%Y-%m-%d %H:%M:%S")
print stamp
logfile = '/home/neelkanth/logs.txt'
dirpath = '/home/neelkanth/PycharmProjects/practice/'
files = os.listdir(dirpath)
fileSize = 0
totalFiles = 0
for file in files:
    if file.startswith('data'):
        fileInfo = os.stat(dirpath + file)
        totalFiles += 1
        fileSize += fileInfo[6]
file = open(logfile, "a")
file.writelines(str(fileSize))
file.close()
