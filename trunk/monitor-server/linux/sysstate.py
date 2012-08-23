#!/usr/bin/env python

def get_server_state(netdict,cpuinfo,cpuload,memfree,tcpcount,syncount):
    state = {}
    use = cpuinfo
    load = cpuload
    mem = memfree
    tcp = tcpcount
    syn = syncount
    inflow = round(float(netdict['inflow'])/1024/1024*8,2)
    outflow = round(float(netdict['outflow'])/1024/1024*8,2)
    inpackage = netdict['inpackage']
    outpackage = netdict['outpackage']
    #cpu
    if int(use) > 50:
        cpuuse = 1
    else:
        cpuuse = 0
    if float(load[1]) > 100:
        cpuload = 1
    elif float(load[2]) > 100:
        cpuload = 1
    else:
        cpuload = 0
    state['use'] = cpuuse
    state['load'] = cpuload
    #mem
    if int(mem) < 10:
        memuse = 1
    else:
        memuse = 0
    state['mem'] = memuse
    #count
    if int(tcp) > 10000:
        count = 1
    elif int(syn) > 300:
        count = 1
    else:
        count = 0
    state['count'] = count
    #network
    if int(inflow) > 300:
        flow = 1
    elif int(outflow) > 1000:
        flow = 1
    else:
        flow = 0
    if int(inpackage) > int(outpackage):
        package = 1
    else:
        package = 0
    state['flow'] = flow
    state['package'] = package
    
    return state
