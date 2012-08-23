from __future__ import division
from django.db import models
from lighten.appinfosys.models import hosts_info
#-*- coding:utf8 -*-
#from lighten.appinfosys.models import hosts_info

# Create your models here.

class networkusage(models.Model):
    mac = models.CharField(max_length=30)
    inpackage = models.CharField(max_length=20)
    outpackage = models.CharField(max_length=20)
    inflow = models.CharField(max_length=20)
    outflow = models.CharField(max_length=20)
    ctime = models.CharField(max_length=20)
    ip = models.ForeignKey(hosts_info)

class cpuusage(models.Model):
    mac = models.CharField(max_length=30)
    use = models.CharField(max_length=10)
    fiveload = models.CharField(max_length=10)
    fifteenload = models.CharField(max_length=10)
    ctime = models.CharField(max_length=20)
    ip = models.ForeignKey(hosts_info)

class memusage(models.Model):
    mac = models.CharField(max_length=30)
    memtotal = models.CharField(max_length=20)
    swaptotal = models.CharField(max_length=20)
    memfree = models.CharField(max_length=20)
    swapfree = models.CharField(max_length=20)
    ctime = models.CharField(max_length=20)
    ip = models.ForeignKey(hosts_info)

class netcount(models.Model):
    mac = models.CharField(max_length=30)
    tcpconnect = models.CharField(max_length=15)
    synconnect = models.CharField(max_length=15)
    ctime = models.CharField(max_length=20)
    ip = models.ForeignKey(hosts_info)

class serverstate(models.Model):
    mac = models.CharField(max_length=30, primary_key=True)
    flow = models.CharField(max_length=5)
    package = models.CharField(max_length=5)
    count = models.CharField(max_length=5)
    mem = models.CharField(max_length=5)
    cpuload = models.CharField(max_length=5)
    cpuuse = models.CharField(max_length=5)
    ip = models.ForeignKey(hosts_info)

class DataHandle(object):
    def __init__(self,mac,date,enddate):
	self.mac = mac
        self.date = date
        self.enddate = enddate
    def SelectNetwork(self):
	inflows = []
	outflows = []
	inpackages = []
	outpackages = []
	maxinflow = []
	maxoutflow = []
	maxinpack = []
	maxoutpack = []
	lsec = {}
	netdata = networkusage.objects.filter(mac=self.mac,ctime__range=(self.date,self.enddate))
	for data in netdata:
    	    inflow = round(float(data.inflow)/1024/1024*8,2)
    	    outflow = round(float(data.outflow)/1024/1024*8,2)		
    	    instr = [data.ctime.encode('utf-8'),inflow]
            outstr = [data.ctime.encode('utf-8'),outflow]
    	    inpack = [data.ctime.encode('utf-8'),data.inpackage.encode('utf-8')]
            outpack = [data.ctime.encode('utf-8'),data.outpackage.encode('utf-8')]
    	    inflows.append(instr)
    	    outflows.append(outstr)
    	    inpackages.append(inpack)
    	    outpackages.append(outpack)
	    maxinflow.append(inflow)
	    maxoutflow.append(outflow)
	    maxinpack.append(float(data.inpackage))
	    maxoutpack.append(float(data.outpackage))
	lsec['inflow'] = "'InFlow': {label: 'InFlow', data: %s}" % inflows
	lsec['outflow'] = "'OutFlow': {label: 'OutFlow', data: %s}" % outflows
	lsec['inpackage'] = "'InPackage': {label: 'InPackage', data: %s}" % inpackages
	lsec['outpackage'] = "'OutPackage': {label: 'OutPackage', data: %s}" % outpackages
	flowdata = lsec['inflow']+',\n'+lsec['outflow']
	packagedata = lsec['inpackage']+',\n'+lsec['outpackage']
	return flowdata,packagedata,max(maxinflow),max(maxoutflow),max(maxinpack),max(maxoutpack)
	#return flowdata,packagedata
	
    def SelectCpu(self):
	fiveload = []
	fifteenload = []
	cpuuse = []
	lsec = {}
	cpudata = cpuusage.objects.filter(mac=self.mac,ctime__range=(self.date,self.enddate))
	for data in cpudata:
	    fivestr = [data.ctime.encode('utf-8'),data.fiveload.encode('utf-8')]
	    fifteenstr = [data.ctime.encode('utf-8'),data.fifteenload.encode('utf-8')]
	    freestr = [data.ctime.encode('utf-8'),data.use.encode('utf-8')]
	    fiveload.append(fivestr)
	    fifteenload.append(fifteenstr)
	    cpuuse.append(freestr)
	lsec['fiveload'] = "'FiveLoad': {label: 'FiveLoad', data: %s}" % fiveload
	lsec['fifteenload'] = "'FifteenLoad': {label: 'FifteenLoad', data: %s}" % fifteenload
	lsec['cpuuse'] = "'CpuUse': {label: 'CpuUse', data: %s}" % cpuuse
	dataload = lsec['fiveload']+',\n'+lsec['fifteenload']
	return dataload,lsec['cpuuse']

    def SelectMem(self):
	mem = []
	swap = []
	memfree = []
	swapfree = []
	lsec = {}
	memdata = memusage.objects.filter(mac=self.mac,ctime__range=(self.date,self.enddate))
	for data in memdata:
	    memstr = [data.ctime.encode('utf-8'),data.memtotal.encode('utf-8')]
	    swapstr = [data.ctime.encode('utf-8'),data.swaptotal.encode('utf-8')]
	    memfreestr = [data.ctime.encode('utf-8'),data.memfree.encode('utf-8')]
	    swapfreestr = [data.ctime.encode('utf-8'),data.swapfree.encode('utf-8')]
	    mem.append(memstr)
	    swap.append(swapstr)
	    memfree.append(memfreestr)
	    swapfree.append(swapfreestr)
	lsec['mem'] = "'MemTotal': {label: 'MemTotal', data: %s}" % mem
	lsec['swap'] = "'SwapTotal': {label: 'SwapTotal', data: %s}" % swap
	lsec['memfree'] = "'MemFree': {label: 'MemFree', data: %s}" % memfree
	lsec['swapfree'] = "'SwapFree': {label: 'SwapFree', data: %s}" % swapfree
	data = lsec['mem']+',\n'+lsec['swap']+',\n'+lsec['memfree']+',\n'+lsec['swapfree']
	return data

    def SelectCount(self):
	tcp = []
	syn = []
	lsec = {}
	countdata = netcount.objects.filter(mac=self.mac,ctime__range=(self.date,self.enddate))
	for data in countdata:
	    tcpstr = [data.ctime.encode('utf-8'),data.tcpconnect.encode('utf-8')]
	    synstr = [data.ctime.encode('utf-8'),data.synconnect.encode('utf-8')]
	    tcp.append(tcpstr)
	    syn.append(synstr)
	lsec['tcp'] = "'Tcp': {label: 'Tcp', data: %s}" % tcp
	lsec['syn'] = "'Syn': {label: 'Syn', data: %s}" % syn
	data = lsec['tcp']+',\n'+lsec['syn']
	return data

    def AllData(self,mac,date,enddate):
	self.mac = mac
        self.date = date
        self.enddate = enddate
	#Get data
	flow,package,inflow,outflow,inpack,outpack = SelectNetwork()
	load,use = SelectCpu()
	mem = SelectMem()
	count = SelectCount()
	#Definition Value
	return flow,package,inflow,outflow,inpack,outpack,load,use,mem,count
