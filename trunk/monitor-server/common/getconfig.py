#!/usr/bin/env python

import os,sys,re
import urllib2
import random
#########################################################
sys.path.append("..")
import tools.config
#########################################################



def read_config(rootpath):
    configfile = rootpath+"/"+"conf"+"/"+"monitorconf.txt"
    if os.path.isfile(configfile):
        return tools.config.parseconfigfile(configfile)
    else:
	print "Conf.txt is not exist!"
    return {}

def read_ip(rootpath):
    configfile = rootpath+"/"+"conf"+"/"+"ip.txt"
    if os.path.isfile(configfile):
        r = open(configfile,'r')
        ip = r.read().strip('\n')
        r.close()
    else:
        try:
            ip = re.search('\d+\.\d+\.\d+\.\d+',urllib2.urlopen("http://www.whereismyip.com").read()).group(0)
        except Exception, err:
            print err
        ipfile = open(configfile,'w')
        ipfile.write(ip)
        ipfile.close()
    return ip

def reconfig(mfile):
    r = open(mfile)
    afile = r.read()
    num = random.randint(0,60)
    refile = re.sub('cnum',str(num),afile)
    r.close()
    refile1 = open(mfile,'w')
    refile1.write(refile)
    refile1.close()
