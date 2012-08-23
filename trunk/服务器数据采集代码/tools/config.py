#!/usr/bin/env python
#-*- coding:utf-8 -*-

import ftplib
import socket

timeout=10
#in seconds
socket.setdefaulttimeout(timeout)
########################################################################
#function
########################################################################
def parseconfigfile(filename):
    try:
        f = open(filename, "r" )
        f.readlines()
        f.seek(0)
    except:
        print "error:致命错误：无法打开文件%s，系统无法继续运行。" % (filename)
        return []
    
    tmpdict = {}
    for line in f.readlines() :
        line = line.rstrip(' ')
        line = line.lstrip(' ')
        if(line[0] != '#' and (line.find('=') != -1)):
            while(line[0] == '\n' or line[0] == '\t' or line[0] == ' '):
                line = line[1:]
            while(line[len(line)-1] == '\n' or line[len(line)-1] == '\t' or line[len(line)-1] == ' '):
                line = line[:-1]
            list1 = line.split('=')
            tmpdict[list1[0]] = list1[1]            
    f.close()

    return tmpdict

if __name__ == '__main__' :
    pass
