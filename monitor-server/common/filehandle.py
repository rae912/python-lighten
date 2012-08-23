# -*- coding: cp936 -*-
import md5
import os,sys,re


def filesearch(filepath):
    f = open(filepath,'r')
    mfile = f.readlines()
    f.close()
    for line in mfile:
        aa = re.search('cnum',line)
        if aa is not None:
            reconfig(filepath)
            break
        else:
            continue
    
