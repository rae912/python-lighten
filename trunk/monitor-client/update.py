# -*- coding: cp936 -*-
########################################################################
#import
########################################################################
import os,sys
import socket
import tarfile,subprocess
############## add custom model ###################
sys.path.append(".")
import tools.config
import tools.version
from common.filemd5 import filesearch
########################################################################
#global
########################################################################
rootpath = os.path.abspath(os.path.dirname(sys.argv[0]))
timeout = 30
#in seconds
socket.setdefaulttimeout(timeout)
########################################################################
#function
######################################################################## 
def install_unpackage(rootpath, tarpath):
    tar = tarfile.open(tarpath)
    names = tar.getnames()
    for name in names:
        if name.find(".svn") != -1:
            continue
        tar.extract(name, path = rootpath)
    tar.close()
    
########################################################################
#main
########################################################################
if __name__ == '__main__' :
    # 设定和改变根目录
    tarpath = ""
    rootpath = "/data0/monitorsys"
    tarpath = rootpath+"/conf/linuxinstall.tar.gz"
    if os.path.exists(rootpath) == False:
        os.mkdir(rootpath)
    os.chdir(rootpath)
    # 下载配置文件比较版本
    config = {}
    tools.config.getconfigfilebyftp('minfo.sinashow.com','showmonitor','linuxshow_#','machine_monitor','verconf.txt',rootpath)
    config = tools.config.parseconfigfile(rootpath+'/'+'conf'+'/'+'verconf.txt')
    culver = tools.version.get_version()
    if culver < config['ver']:# 解包
        if tools.config.getconfigfilebyftp('minfo.sinashow.com','showmonitor','linuxshow_#','machine_monitor','linuxinstall.tar.gz',rootpath):
            install_unpackage(rootpath, tarpath)
	    filesearch(rootpath+'/conf/monitorconf.txt')
            sh = subprocess.Popen(args = "/bin/sh"+" "+rootpath+"/tools/installset.sh",shell=True,stdout=subprocess.PIPE)
            sh.stdout.close()
    sys.exit(0)
