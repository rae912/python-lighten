#!/usr/bin/env python

import os,re

def http_status():
    cmd = "netstat -nap|grep httpd"
    http = os.popen(cmd,"r")
    httpfile = http.readlines()
    http.close()
    hdict ={}
    for line in httpfile:
        line = re.sub(r'\s+',' ',line)
        tmplist = line.strip().split(' ')
        if len(tmplist) == 7:
            handport = tmplist[3]
            handpid = tmplist[6]
            portstr = re.findall(r':\d+',handport)
            port = re.findall(r'\d+',portstr[0])
            pid = re.findall(r'\d+',handpid)
            hdict['port'] = port[0]
            hdict['pid'] = pid[0]
            break
    if hdict:
        hdict['status'] = 0
        hdict['service'] = 'apache'
    else:
        hdict = {'service':'apache','status':1,'port':0,'pid':0}
    return hdict

def mysql_status():
    cmd = "netstat -nap|grep mysql"
    mysql = os.popen(cmd,"r")
    mysqlfile = mysql.readlines()
    mysql.close()
    hdict = {}
    for line in mysqlfile:
        line = re.sub(r'\s+',' ',line)
        tmplist = line.strip().split(' ')
        if len(tmplist) == 7:
            handport = tmplist[3]
            handpid = tmplist[6]
            portstr = re.findall(r':\d+',handport)
            port = re.findall(r'\d+',portstr[0])
            pid = re.findall(r'\d+',handpid)
            hdict['port'] = port[0]
            hdict['pid'] = pid[0]
            break
    if hdict:
        hdict['status'] = 0
        hdict['service'] = 'mysql'
    else:
        hdict = {'service':'mysql','status':1,'port':0,'pid':0}
    return hdict

def all_status():
    status = {'http':http_status(),'mysql':mysql_status()}
    return status

if __name__ == '__main__':
    a = http_status()
    print a
    print '-------------------'
    b = mysql_status()
    print b