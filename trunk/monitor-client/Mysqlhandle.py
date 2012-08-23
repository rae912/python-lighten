#!/usr/bin/env python
#-*- coding:utf-8 -*-

from LightenMysql import TestMysql
from DataHandle import StrCom
import time

class MysqlHandle:
    def __init__(self):
	self.time = ''
    def DataHandle(self, data):
        str = data.split('+')
        if str[0] == '1':
	    Mysql = TestMysql()
	    ip = str[2].split('.')
	    netip = '%s.%s.%s' % (ip[0],ip[1],ip[2])
            sctnet = "select netname from appinfosys_ipnet_info where ipnet = '%s'" % netip
	    netname = Mysql.SelectMysql(sctnet)
            select = "select * from appinfosys_hosts_info where mac = '%s'" % str[2]
            sql = "insert into appinfosys_hosts_info values('%s','%s','%s','%s')" % (str[1],str[2],netname[0][0],str[3])
            update = "update appinfosys_hosts_info set ip = '%s',idc = '%s',infosys = '%s' where mac = '%s'" % (str[2],netname[0][0],str[3],str[1])
            InfoData(str,select,sql,update)
        if str[0] == '2':
            select = "select * from appinfosys_cpu_info where mac = '%s'" % str[1]
            sql = "insert into appinfosys_cpu_info values('%s','%s','%s','%s','%s')" % (str[1],str[2],str[3],str[4],str[1])
            update = "update appinfosys_cpu_info set mname = '%s',mcores = '%s',mclockspeed = '%s' where mac = '%s'" % (str[2],str[3],str[4],str[1])
            InfoData(str,select,sql,update)
        if str[0] == '3':
            select = "select * from appinfosys_disk_info where mac = '%s' AND mfs_name = '%s'" %  (str[1],str[3])
            sql = "insert into appinfosys_disk_info values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s')" % (str[1],str[2],str[3],str[4],str[5],str[6],str[7],str[1])
            update = "update appinfosys_disk_info set mcaption = '%s',mfs_size = '%s',mfs_free = '%s',mfs_use = '%s',mfs_used  = '%s' where mac = '%s' AND mfs_name = '%s'" % (str[2],str[4],str[5],str[6],str[7],str[1],str[3])
            DiskData(select,sql,update)
        if str[0] == '4':
            select = "select * from appinfosys_network_info where mac = '%s'" % str[1]
            sql = "insert into appinfosys_network_info values('%s','%s','%s','%s','%s','%s','%s')" % (str[1],str[2],str[3],str[4],str[5],str[6],str[1])
            update = "update appinfosys_network_info set mname = '%s',mmask = '%s',mmtu = '%s',mdrive = '%s',mmodel = '%s' where mac = '%s'" % (str[2],str[3],str[4],str[5],str[6],str[1])
            InfoData(str,select,sql,update)
        if str[0] == '5':
            select = "select * from appnetworksys_serverstatus where mac = '%s' AND service_name = '%s'" % (str[1],str[2])
            sql = "insert into appnetworksys_serverstatus values(NULL,'%s','%s','%s','%s','%s','%s')" % (str[1],str[2],str[3],str[4],str[5],str[1])
            update = "update appnetworksys_serverstatus set service_name = '%s',service_port = '%s',service_pid = '%s',service_status = '%s' where mac = '%s'" % (str[2],str[3],str[4],str[5],str[1])
	    str.append(str[1])
            ListData(str,select,sql,update)
	if str[0] == '6':
            select = "select * from appnetworksys_connections where mac = '%s'" % str[1]
            sql = "insert into appnetworksys_connections values('%s','%s','%s','%s')" % (str[1],str[2],str[3],str[1])
            update = "update appnetworksys_connections set connections = '%s',ports = '%s' where mac = '%s'" % (str[2],str[3],str[1])
            InfoData(str,select,sql,update)
	if str[0] == '7':
	    self.time = time.strftime("%Y-%m-%d %H:%M:%S")
	    Mysql = TestMysql()
	    str.append(self.time)
	    sql = "insert into appmonitorsys_networkusage values(NULL,'%s','%s','%s','%s','%s','%s','%s')" % (str[1],str[2],str[3],str[4],str[5],str[6],str[1])
	    Mysql.ConnectMysql(sql)
	if str[0] == '8':
	    self.time = time.strftime("%Y-%m-%d %H:%M:%S")
	    Mysql = TestMysql()
	    str.append(self.time)
	    sql = "insert into appmonitorsys_cpuusage values(NULL,'%s','%s','%s','%s','%s','%s')" % (str[1],str[2],str[3],str[4],str[5],str[1])
	    Mysql.ConnectMysql(sql)
	if str[0] == '9':
	    self.time = time.strftime("%Y-%m-%d %H:%M:%S")
	    Mysql = TestMysql()
	    str.append(self.time)
	    sql = "insert into appmonitorsys_memusage values(NULL,'%s','%s','%s','%s','%s','%s','%s')" % (str[1],str[2],str[3],str[4],str[5],str[6],str[1])
	    Mysql.ConnectMysql(sql)
	if str[0] == '10':
            self.time = time.strftime("%Y-%m-%d %H:%M:%S")
            Mysql = TestMysql()
            str.append(self.time)
            sql = "insert into appmonitorsys_netcount values(NULL,'%s','%s','%s','%s','%s')" % (str[1],str[2],str[3],str[4],str[1])
            Mysql.ConnectMysql(sql)
	if str[0] == '11':
            select = "select * from appmonitorsys_serverstate where mac = '%s'" % str[1]
            sql = "insert into appmonitorsys_serverstate values('%s','%s','%s','%s','%s','%s','%s','%s')" % (str[1],str[2],str[3],str[4],str[5],str[6],str[7],str[1])
            update = "update appmonitorsys_serverstate set flow = '%s',package = '%s',count = '%s',mem = '%s',cpuload = '%s',cpuuse = '%s' where mac = '%s'" % (str[2],str[3],str[4],str[5],str[6],str[7],str[1])
            InfoData(str,select,sql,update)


def InfoData(str,select,sql,update):
	Mysql = TestMysql()
	try:
	    connstr = Mysql.SelectMysql(select)
	    com = StrCom()
	    com = com.strHandle(str,connstr)
	    if not com:
		Mysql.ConnectMysql(update)
	    else:
		pass
	except:
	    Mysql.ConnectMysql(sql)

def DiskData(select,sql,update):
    Mysql = TestMysql()
    try:
        connstr = Mysql.SelectMysql(select)
        if connstr[0]:
            Mysql.ConnectMysql(update)
        else:
            Mysql.ConnectMysql(sql)
    except:
        Mysql.ConnectMysql(sql)

def ListData(str,select,sql,update):
        Mysql = TestMysql()
        try:
            connstr = Mysql.SelectMysql(select)
            com = StrCom()
            com = com.ListHandle(str,connstr)
            if not com:
                Mysql.ConnectMysql(update)
            else:
                pass
        except:
            Mysql.ConnectMysql(sql)

def DictData(str,select,sql,update):
    Mysql = TestMysql()
    try:
	connstr = Mysql.DictMysql(select)
	print connstr
    except:
	pass
