#!/usr/bin/env python
#-*- coding:utf-8 -*-
########################################################################
import urllib
########################################################################
# 协议编号定义
PKTYPE_HOSTINFO = 1   
PKTYPE_CPUINFO = 2
PKTYPE_DISKINFO = 3
PKTYPE_NETINFO = 4
PKTYPE_STATUS = 5
PKTYPE_CONNPORT = 6
PKTYPE_NETWORKINFO = 7
PKTYPE_CPUPROC = 8
PKTYPE_MEMPROC = 9
PKTYPE_NETCOUNT = 10
PKTYPE_STATE = 11
########################################################################
class hostinfo:
    def __init__(self):
        self.params = ""
        self.mac = ""
        self.ip = ""
        self.infosys = ""
    def Serialize(self,PackType = PKTYPE_HOSTINFO):
        try:
            self.params = "%s+%s+%s+%s" % (PackType,self.mac,self.ip,self.infosys)
            return True
        except:
            return False

class cpuinfo:
    def __init__(self):
        self.params = ""
        self.mac = ""
        self.mname = ""         #cpu名称
        self.mcores = ""        #cpu物理核个数
        self.mclockspeed = ""   #cpu主频
    def Serialize(self, PackType = PKTYPE_CPUINFO):
        try:
            self.params = "%s+%s+%s+%s+%s" % (PackType,self.mac,self.mname,self.mcores,self.mclockspeed)
            return True
        except:
            return False
        
class diskinfo:
    def __init__(self):
        self.params = ""
        self.mac = ""
        self.mcaption = ""      #磁盘名称
        self.mfs_name = ""         #磁盘尺寸
        self.mfs_size = ""
        self.mfs_free = ""
        self.mfs_use = ""
        self.mfs_used = ""
    def Serialize(self, PackType = PKTYPE_DISKINFO):
        try:
            self.params = "%s+%s+%s+%s+%s+%s+%s+%s" % (PackType,self.mac,self.mcaption,self.mfs_name,self.mfs_size,self.mfs_free,self.mfs_use,self.mfs_used)
            return True
        except:
            return False

class netinfo:
    def __init__(self):
        self.params = ""
        self.mac = ""
        self.mname = "" 
        self.mmask = ""
        self.mmtu = ""
        self.mdrive = ""
        self.mmodel = ""
    def Serialize(self, PackType = PKTYPE_NETINFO):
        try:
            self.params = "%s+%s+%s+%s+%s+%s+%s" % (PackType,self.mac,self.mname,self.mmask,self.mmtu,self.mdrive,self.mmodel)
            return True
        except:
            return False
        
class status:
    def __init__(self):
        self.params = ""
        self.mac = ""
        self.service_name = ""
        self.service_port = ""
        self.service_pid = ""
        self.service_status =""    
    def Serialize(self, PackType = PKTYPE_STATUS):
        try:
            self.params = "%s+%s+%s+%s+%s+%s" % (PackType,self.mac,self.service_name,self.service_port,self.service_pid,self.service_status)
            return True
        except:
            return False

class connport:
    def __init__(self):
        self.params = ""
        self.mac = ""
        self.connections = ""
        self.ports = ""
    def Serialize(self, PackType = PKTYPE_CONNPORT):
        try:
            self.params = "%s+%s+%s+%s" % (PackType,self.mac,self.connections,self.ports)
            return True
        except:
            return False

class networkinfo:
    def __init__(self):
        self.params = ""
        self.mac = ""
        self.inpackage = ""
        self.outpackage = ""
        self.inflow = ""
        self.outflow = ""
    def Serialize(self, PackType = PKTYPE_NETWORKINFO):
        try:
            self.params = "%s+%s+%s+%s+%s+%s" % (PackType,self.mac,self.inpackage,self.outpackage,self.inflow,self.outflow)
            return True
        except:
            return False

class cpuproc:
    def __init__(self):
        self.params = ""
        self.mac = ""
        self.use = ""
        self.fiveload = ""
        self.fifteenload = "" 
    def Serialize(self, PackType = PKTYPE_CPUPROC):
        try:
            self.params = "%s+%s+%s+%s+%s" % (PackType,self.mac,self.use,self.fiveload,self.fifteenload)
            return True
        except:
            return False
        
class memproc:
    def __init__(self):
        self.params = ""
        self.mac = ""
        self.memtotal = ""
        self.swaptotal = ""
        self.memfree = ""
        self.swapfree = ""
    def Serialize(self, PackType = PKTYPE_MEMPROC):
        try:
            self.params = "%s+%s+%s+%s+%s+%s" % (PackType,self.mac,self.memtotal,self.swaptotal,self.memfree,self.swapfree)
            return True
        except:
            return False

class netcount:
    def __init__(self):
        self.params = ""
        self.mac = ""
        self.tcpconnect = ""
        self.synconnect = ""
    def Serialize(self, PackType = PKTYPE_NETCOUNT):
        try:
            self.params = "%s+%s+%s+%s" % (PackType,self.mac,self.tcpconnect,self.synconnect)
            return True
        except:
            return False

class state:
    def __init__(self):
        self.params = ""
        self.mac = ""
        self.flow = ""
        self.package = ""
        self.count = ""
        self.mem = ""
        self.cpuload = ""
        self.cpuuse = ""
    def Serialize(self, PackType = PKTYPE_STATE):
        try:
            self.params = "%s+%s+%s+%s+%s+%s+%s+%s" % (PackType,self.mac,self.flow,self.package,self.count,self.mem,self.cpuload,self.cpuuse)
            return True
        except:
            return False


if __name__ == "__main__":
    pass
