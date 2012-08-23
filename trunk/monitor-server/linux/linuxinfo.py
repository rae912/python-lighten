#!/usr/bin/env python
#-*- coding:utf-8 -*-
######################################################
#import
import sys
import datetime
import logging
import socket
############## add custom model ###################
sys.path.append("..")
import common.packdef
import linux.syscpu
import linux.sysmemory
import linux.sysdisk
import linux.sysnetwork
import linux.sysstatus
from linux.sysstate import get_server_state
######################################################
# global
######################################################
logger = logging.getLogger('client')
#set timeout
timeout=10
#in seconds
socket.setdefaulttimeout(timeout)
######################################################
# function
######################################################
def senddate(ip, port, date):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send(date)
        s.close()
    except Exception, err:
        print err
######################################################
class linux_info:
    def __init__(self):
        self.cpuinfo = {}
        self.cpuusage= []
        self.memoryinfo = {}
        self.diskinfo = {}
        self.fsinfo = []
        self.networkinfo = []
        self.tcpvalues = 0
        self.osinfo = ""
        self.serverinfo = ""
        self.comment = ""
        self.version = ""
        self.status = ""
        # local value
        self.nettraffic = 0
        self.localipinfo = {}
        # warning flag
        self.cpuloadwarning = 0
        self.memorywarnging = 0
        self.diskspacewarning = 0
        self.nettcpwarning = 0
        self.netsynwarning = 0
        self.nettrafficwarning = 0
        
    def init_info(self):
        self.cpuinfo = linux.syscpu.get_cpu_info()         #cpu物理信息
        #print self.cpuinfo
        self.cpuload = linux.syscpu.get_cpu_load()         #cpu负载
        #print self.cpuload
        self.cpuusage = linux.syscpu.get_cpu_usage()       #cpu使用率
        #print self.cpuusage
        self.memoryinfo = linux.sysmemory.get_memory_info()#物理内存使用率
        #print self.memoryinfo
        self.diskinfo = linux.sysdisk.get_disk_info()      #disk物理信息
        #print self.diskinfo
        self.fsinfo = linux.sysdisk.get_fs_info()          #分区信息
        #print self.fsinfo
        self.networkinfo = linux.sysnetwork.get_network_info()# 获取网络信息
        #print self.networkinfo
        self.tcpvalues = linux.sysnetwork.tcpvalues()      #获取tcp连接数信息
        #print self.tcpvalues
        self.synvalues = linux.sysnetwork.synvalues()      #获取syn连接数信息
        #print self.synvalues
        self.status = linux.sysstatus.all_status()        #获取服务状态
        #print self.status
        self.ports = linux.sysnetwork.sysport()           #获取服务器开启的端口
        #print self.ports

    def check_stat(self,ip):
        for netdict in  self.networkinfo:
            if str(netdict["IPAddress"]) == str(ip):
                self.localipinfo["Description"] = netdict["Description"]
                self.localipinfo["IPAddress"] = netdict["IPAddress"]
                self.localipinfo["IPSubnet"] = netdict["IPSubnet"]
                self.localipinfo["MAC"] = netdict["MAC"]
                self.localipinfo["MTU"] = netdict["MTU"]
                self.localipinfo["inflow"] = netdict["inflow"]
                self.localipinfo["outflow"] = netdict["outflow"]
                self.localipinfo["inpackage"] = netdict["inpackage"]
                self.localipinfo["outpackage"] = netdict["outpackage"]
                self.localipinfo["netdirver"] = netdict["netdirver"]
                self.localipinfo["netdesc"] = netdict["netdesc"]
            else:
                self.localipinfo["IntranetIP"] = netdict["IPAddress"]
                continue  
    def report_info(self,config):
        num = config["num"]
        ip = config["repser_ip"]
        port = int(config["repser_port"])
        curmin = datetime.datetime.now().minute
        hour = datetime.datetime.now().hour
        if(0 == curmin % 1): 
            self.send_status(ip, port)
            self.send_connport(ip, port)
            self.send_networkinfo(ip, port)
            self.send_cpuproc(ip, port)
            self.send_memproc(ip, port)
            self.send_netcount(ip, port)
	    self.send_state(ip, port)
        if(0 == curmin % 20):
            self.send_diskinfo(ip, port)  #分区信息 20分钟上报一次
        #if(int(hour) == 1 and int(curmin) == int(num)): 
            self.send_hostinfo(ip, port)
            self.send_cpuinfo(ip, port)
            self.send_netinfo(ip, port)
                        
    def send_hostinfo(self, ip, port):
        #logininfo
        SendPkg = common.packdef.hostinfo()
        SendPkg.mac = self.localipinfo["MAC"]
        SendPkg.ip = self.localipinfo["IPAddress"]
        SendPkg.infosys = self.version["mos_system"]
        if not SendPkg.Serialize():
            print "type:1 error"
        else:
            print SendPkg.params
            senddate(ip, port, SendPkg.params)
        
    def send_cpuinfo(self, ip, port):
        #cpuinfo
        SendPkg = common.packdef.cpuinfo()
        SendPkg.mac = self.localipinfo["MAC"]
        SendPkg.mname = self.cpuinfo["model name"]
        SendPkg.mcores = str(self.cpuinfo["cpu cores"])+"*"+str(self.cpuinfo["phynum"])
        SendPkg.mclockspeed = self.cpuinfo["cpu MHz"]
        if not SendPkg.Serialize():
            print "type:2 error"
        else:
            print SendPkg.params
            senddate(ip, port, SendPkg.params)
            
    def send_diskinfo(self, ip, port):
        #fsinfo[]
        for finfo in self.fsinfo:
            SendPkg = common.packdef.diskinfo()
            SendPkg.mac = self.localipinfo["MAC"]
            SendPkg.mcaption = self.diskinfo
            SendPkg.mfs_name = finfo[5]
            SendPkg.mfs_size = finfo[1]
            SendPkg.mfs_free = finfo[3]
            SendPkg.mfs_use = finfo[2]
            SendPkg.mfs_used = finfo[4][:-1]
            if not SendPkg.Serialize():
                print "type:3 error"
            else:
                print SendPkg.params
                senddate(ip, port, SendPkg.params)

    def send_netinfo(self, ip, port):
        SendPkg = common.packdef.netinfo()
        SendPkg.mac = self.localipinfo["MAC"]
        SendPkg.mname = self.localipinfo["IntranetIP"]
        SendPkg.mmask = self.localipinfo["IPSubnet"]
        SendPkg.mmtu = self.localipinfo["MTU"]
        SendPkg.mdrive = self.localipinfo["netdirver"]
        SendPkg.mmodel = self.localipinfo["netdesc"]
        if not SendPkg.Serialize():
            print "type:4 error"
        else:
            print SendPkg.params
            senddate(ip, port, SendPkg.params)
    
    def send_status(self, ip, port):
        for key in self.status.keys():
            SendPkg = common.packdef.status()
            SendPkg.mac = self.localipinfo["MAC"]
            SendPkg.service_name = self.status[key]['service']
            SendPkg.service_port = self.status[key]['port']
            SendPkg.service_pid = self.status[key]['pid']
            SendPkg.service_status = self.status[key]['status']
            if not SendPkg.Serialize():
                print "type:5 error"
            else:
                print SendPkg.params
                senddate(ip, port, SendPkg.params)
                
    def send_connport(self, ip, port):
        SendPkg = common.packdef.connport()
        SendPkg.mac = self.localipinfo["MAC"]
        SendPkg.connections = self.tcpvalues
        SendPkg.ports = self.ports
        if not SendPkg.Serialize():
            print "type:6 error"
        else:
            print SendPkg.params
            senddate(ip, port, SendPkg.params)
    def send_networkinfo(self, ip, port):
        #network
        SendPkg = common.packdef.networkinfo()
        SendPkg.mac = self.localipinfo["MAC"]
        SendPkg.inpackage = self.localipinfo["inpackage"]
        SendPkg.outpackage = self.localipinfo["outpackage"]
        SendPkg.inflow = self.localipinfo["inflow"]
        SendPkg.outflow = self.localipinfo["outflow"]
        if not SendPkg.Serialize():
            print "type:7 error"
        else:
            print SendPkg.params
            senddate(ip, port, SendPkg.params)
    
    def send_cpuproc(self, ip, port):
        SendPkg = common.packdef.cpuproc()
        SendPkg.mac = self.localipinfo["MAC"]
        SendPkg.use = self.cpuusage
        SendPkg.fiveload = int(float(self.cpuload[1]))
        SendPkg.fifteenload = int(float(self.cpuload[2]))
        if not SendPkg.Serialize():
            print "type:8 error"
        else:
            print SendPkg.params
            senddate(ip, port, SendPkg.params)
    def send_memproc(self, ip, port):
        SendPkg = common.packdef.memproc()
        SendPkg.mac = self.localipinfo["MAC"]
        SendPkg.memtotal = self.memoryinfo["MemTotal"]
        SendPkg.swaptotal = self.memoryinfo["SwapTotal"]
        SendPkg.memfree = self.memoryinfo["MemFree"]
        SendPkg.swapfree = self.memoryinfo["SwapFree"]
        if not SendPkg.Serialize():
            print "type:9 error"
        else:
            print SendPkg.params
            senddate(ip, port, SendPkg.params)      
    def send_netcount(self, ip, port):
        SendPkg = common.packdef.netcount()
        SendPkg.mac = self.localipinfo["MAC"]
        SendPkg.tcpconnect = self.tcpvalues
        SendPkg.synconnect = self.synvalues
        if not SendPkg.Serialize():
            print "type:10 error"
        else:
            print SendPkg.params
            senddate(ip, port, SendPkg.params)
    def send_state(self, ip, port):
        state = get_server_state(self.localipinfo,self.cpuusage,self.cpuload,self.memoryinfo["MemFree"],self.tcpvalues,self.synvalues)
        SendPkg = common.packdef.state()
        SendPkg.mac = self.localipinfo["MAC"]
        SendPkg.flow = state['flow']
        SendPkg.package = state['package']
        SendPkg.count = state['count']
        SendPkg.mem = state['mem']
        SendPkg.cpuload = state['load']
        SendPkg.cpuuse = state['use']
        if not SendPkg.Serialize():
            print "type:11 error"
        else:
            print SendPkg.params
            senddate(ip, port, SendPkg.params)
        
if __name__ == "__main__":
    linuxobj = linux_info()
    #获取window信息
    linuxobj.init_info()
