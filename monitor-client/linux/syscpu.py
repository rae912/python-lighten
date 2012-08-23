#!/usr/bin/env python

import os
import sys
import time

def get_cpu_info() :
    """get cpu info from /proc/cpuinfo"""
    cpuinfo = "/proc/cpuinfo"
    try:
        f = open(cpuinfo, "r")
        cpufile = f.readlines()
        f.close()
    except:
        print "error:%s" % (cpuinfo)
        return {}
    tmpdict = {}
    physical = []
    for line in cpufile:
        tmplist = []
        tmplist = line.strip().split(":")
        if len(tmplist) == 2 :
            if tmplist[0].strip() == "model name":
                tmpdict[tmplist[0].strip()] = tmplist[1].strip()
            elif tmplist[0].strip() == "cpu cores":
                tmpdict[tmplist[0].strip()] = tmplist[1].strip()
            elif tmplist[0].strip() == "cpu MHz":
                tmpdict[tmplist[0].strip()] = tmplist[1].strip()
            elif tmplist[0].strip() == "physical id":
                physical.append(tmplist[1].strip())
    phyid = len(list(set(physical)))
    tmpdict['phynum'] = phyid
    try:
	cores = tmpdict['cpu cores']
	pass
    except:
	tmpdict['cpu cores'] = '0'
    return tmpdict

def _read_cpu_usage():
    """Read the current system cpu usage from /proc/stat"""
    statfile = "/proc/stat"
    try:
        f = open(statfile, 'r')
        lines = f.readlines()
    except:
        print "error:%s" % (statfile)
        return []
    for line in lines:
        tmplist = line.split()
        if len(tmplist) < 5:
            continue
        if tmplist[0].startswith('cpu'):
            return tmplist
    f.close()
    return []

def get_cpu_usage():
    """get cpu avg used by percent"""
    cpustr=_read_cpu_usage()
    if not cpustr:
        return 0
    usni1=long(cpustr[1])+long(cpustr[2])+long(cpustr[3])+long(cpustr[5])+long(cpustr[6])+long(cpustr[7])+long(cpustr[4])
    usn1=long(cpustr[1])+long(cpustr[2])+long(cpustr[3])
    sleep=1
    time.sleep(sleep)
    cpustr=_read_cpu_usage()
    if not cpustr:
        return 0
    usni2=long(cpustr[1])+long(cpustr[2])+float(cpustr[3])+long(cpustr[5])+long(cpustr[6])+long(cpustr[7])+long(cpustr[4])
    usn2=long(cpustr[1])+long(cpustr[2])+long(cpustr[3])
    cpuper=(usn2-usn1)/(usni2-usni1)
    return int(100*cpuper)

def get_cpu_load() :
    proc_path = "/proc/loadavg"
    try :
        f = open( proc_path, "r" )
        f.readlines()
        f.seek(0)
    except:
        print "Error:%s" % (proc_path)
        return []
    i=0
    for line in f.readlines() :
        tmplist = line.split(' ');
        try:
            if(len(tmplist) == 5):
                tmplist[4] = tmplist[4][:-1]
                f.close()
                return tmplist
        except:
            print 'have error line'
            continue
    f.close()
    return []

if __name__ == "__main__":
    a = {}
    a = get_cpu_info()
    print a
    print '--------------------------'
    b = get_cpu_usage()
    print b
    print '--------------------------'
    c = get_cpu_load()
    print c
