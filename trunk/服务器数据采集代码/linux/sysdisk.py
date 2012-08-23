#!/usr/bin/env python

import sys
import os


def get_disk_info() :
    proc_path = "/proc/partitions"
    try :
        f = open( proc_path, "r" )
        f.readlines()
        f.seek(0)
    except:
        print "open files error!"
        return {} 
    partitions = []
    for line in f.readlines() :
        line = line.strip()
        list = line.split()
        if line  == "" or line.startswith( "major" ) or len(list) != 4 :
            continue
        if list[3].isalpha() :
            size = int(int( list[2] ) * 1024 / 1000 / 1000 / 1000)
            partitions.append(size)
        elif (list[3].find('/')!=-1 and list[3].find('p') == -1) :
            size = int(int( list[2] ) * 1024 / 1000 / 1000 / 1000)
            partitions.append(size)           
    f.close()
    num = len(partitions)
    sizenum = 0
    if num > 1:
        for i in range(num):
            if i == 0:
                sizenum = int(partitions[i])
            else:
                sizenum = int(partitions[i]) + int(sizenum)
    else:
        sizenum = int(partitions[0])
    disksize = str(sizenum)+"G|"+str(num)
    return disksize

def get_fs_info() :
    try :
        pipe = os.popen( "/bin/df -h ", "r" )
    except:
        print "command error!"
        return []
    pipe.readline()
    exclist = ''
    retlist = []
    getlen=0
    for line in pipe.readlines():
        line = line.strip()
        tmplist = []
        tmplist = line.split()
        getlen = len(tmplist)
        if getlen == 6:
            retlist.append(tmplist)
            getlen=0
        elif getlen == 1:
            exclist = tmplist
            getlen=0
        elif getlen == 5:
            exclist = exclist+tmplist
            retlist.append(exclist)
            exclist = ''
            getlen=0
    pipe.close()
    return retlist

if __name__ == "__main__":
    disk = get_disk_info()
    print disk
    print '--------------------------------------'
    fs = get_fs_info()
    print fs

