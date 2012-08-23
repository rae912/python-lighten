#!/usr/bin/env python

from __future__ import division
import os,re
import sys
import time
import socket
import array
import fcntl
import struct
import datetime

def find_all_interface_names() :
    SIOCGIFCONF = 0x8912    
    ifreq_size = 24 + 2 * len( struct.pack( 'P', 0 ) )
    max_possible = 128
    bytes = max_possible * ifreq_size

    ifreq_buf = array.array( 'B', '\0' * bytes )
    ifconf = struct.pack( 'iP', bytes, ifreq_buf.buffer_info()[0] )

    s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    ret = fcntl.ioctl( s.fileno(), SIOCGIFCONF, ifconf )
    s.close()

    ifc_len, ifreq = struct.unpack( 'iP', ret )
    names = []
    for i in range( 0, ifc_len, ifreq_size ):
        ifr_name = ( ifreq_buf.tostring()[ i : i + ifreq_size ] )[:16]
        names.append( ifr_name.split( '\0', 1 )[0] )

    return names

def get_hwaddr_for_interface( ifname ) :
    SIOCGIFHWADDR = 0x8927    
    ifreq = struct.pack( '16sH14s', ifname, 0, '' )

    s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    ret = fcntl.ioctl( s.fileno(), SIOCGIFHWADDR, ifreq )
    s.close()

    hwaddr = struct.unpack( '16sH14B', ret )[2:]
    return "%02X:%02X:%02X:%02X:%02X:%02X"\
        % ( hwaddr[0], hwaddr[1], hwaddr[2], hwaddr[3], hwaddr[4], hwaddr[5] )

def get_address_for_interface( ifname ) :
    SIOCGIFADDR = 0x8915
    ifreq = struct.pack( '16sH14s', ifname, 0, '' )

    s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    ret = fcntl.ioctl( s.fileno(), SIOCGIFADDR, ifreq )
    s.close()

    addr = struct.unpack( '16sH14B', ret )[2:]

    return "%d.%d.%d.%d" %( addr[2], addr[3], addr[4], addr[5] )

def get_netmask_for_interface( ifname ):
    SIOCGIFNETMASK = 0x891B
    ifreq = struct.pack( '16sH14s', ifname, 0, '' )

    s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    ret = fcntl.ioctl( s.fileno(), SIOCGIFNETMASK, ifreq )
    s.close()

    addr = struct.unpack( '16sH14B', ret )[2:]
    return "%d.%d.%d.%d" %( addr[2], addr[3], addr[4], addr[5] )
    
def get_brdaddr_for_interface( ifname ):
    SIOCGIFBRDADDR = 0x8919
    ifreq = struct.pack( '16sH14s', ifname, 0, '' )

    s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    ret = fcntl.ioctl( s.fileno(), SIOCGIFBRDADDR, ifreq )
    s.close()

    addr = struct.unpack( '16sH14B', ret )[2:]
    return "%d.%d.%d.%d" %( addr[2], addr[3], addr[4], addr[5] )

def get_mtu_for_interface( ifname ):
    SIOCGIFMTU = 0x8921    
    ifreq = struct.pack( '16si', ifname, 0 )

    s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    ret = fcntl.ioctl( s.fileno(), SIOCGIFMTU, ifreq )
    s.close()

    ifname, mtu = struct.unpack( '16si', ret )
    return mtu   

def getCurFlow( ifname ):
    rflow = 0
    sflow = 0
    rpkg = 0
    spkg = 0

    flow = open('/proc/net/dev')
    lines = flow.readlines()
    flow.close()

    devinfodict = {}
    for line in lines:
        intflist = line.split(':')
        if len(intflist) == 2:
            if intflist[0].strip() == ifname:
                #print intflist[0].strip()
                itemlist = intflist[1].split()
                #print "R:",itemlist[0],itemlist[1]
                #print "T:",itemlist[8],itemlist[9]
                rflow = itemlist[0]
                rpkg = itemlist[1]
                sflow = itemlist[8]
                spkg = itemlist[9]
    return int(rflow), int(sflow), int(rpkg), int(spkg)

def getTraffic( ifname ):
    rflow = 0
    sflow = 0
    rflow1 = 0
    sflow1 = 0
    rflow2 = 0
    sflow2 = 0
    rpkg = 0
    spkg = 0
    rpkg1 = 0
    spkg1 = 0
    rpkg2 = 0
    spkg2 = 0
    rflow1, sflow1, rpkg1, spkg1 = getCurFlow(ifname)
    sleep=2
    time.sleep(sleep)
    rflow2, sflow2, rpkg2, spkg2 = getCurFlow(ifname)
    rflow = rflow2 - rflow1
    sflow = sflow2 - sflow1
    rflow = rflow / 2
    sflow = sflow / 2
    rpkg = rpkg2 - rpkg1
    spkg = spkg2 - spkg1
    rpkg = rpkg / 2
    spkg = spkg / 2
    return rflow, sflow, rpkg, spkg

def net_info():
    cmd = "/usr/sbin/kudzu --probe --class=network"
    try:
        pipe = os.popen(cmd,"r")
    except:
        print "Kudzu Error exit"
        return 0
    netfile = pipe.readlines()
    pipe.close()
    netdirver = []
    netdesc = []
    for line in netfile:
        tmplist = []
        tmplist = line.strip().split(":")
        if len(tmplist) == 2 :
            if tmplist[0].strip() == "driver":
                netdirver.append(tmplist[1].strip())
            if tmplist[0].strip() == "desc":
                descfile = tmplist[1].split(' ')
                for i in range(len(descfile)):
                    desc1 = re.findall(r'\d+\w+',descfile[i])
                    desc2 = re.findall(r'\w+\d+',descfile[i])
                    if desc1:
                        netdesc.append(descfile[i])
                        break
                    elif desc2:
                        netdesc.append(descfile[i])
                        break
                    else:
                        continue
    dirver = list(set(netdirver))
    netdi = ''
    if len(dirver) > 0:
        for i in range(len(dirver)):
            if i == 0:
                netdi = str(dirver[i])
            else:
                netdi = netdi+","+str(dirver[i])
    else:
        netdi = str(dirver[i])
    desc = list(set(netdesc))
    netde = ''
    if len(desc) > 0:
        for i in range(len(desc)):
            if i == 0:
                netde = str(desc[i])
            else:
                netde = netde+","+str(desc[i])
    else:
        netde = str(desc[i])
    return netdi,netde

def get_network_info():
    tmplist = []
    allintfacename = find_all_interface_names()
    for line in allintfacename:
        tmpdict = {}
        tmpdict["Description"] = line
        tmpdict["IPAddress"] = get_address_for_interface(line)
        tmpdict["IPSubnet"] = get_netmask_for_interface(line)
        tmpdict["MAC"] = get_hwaddr_for_interface(line)
        tmpdict["MTU"] = get_mtu_for_interface(line)
        tmpdict["inflow"],tmpdict["outflow"],tmpdict["inpackage"],tmpdict["outpackage"] = getTraffic(line)
        tmpdict["netdirver"],tmpdict["netdesc"] = net_info()
        tmplist.append(tmpdict)
    return tmplist

def tcpvalues():
    cmd = "/bin/netstat -tanp|grep 'ESTABLISHED'|grep -v '127.0.0.1'|wc -l"
    #print cmd
    try :
        pipe = os.popen(cmd , "r" )
    except:
        print "can't system command exit"
        return 0
        
    line = pipe.readlines()
    pipe.close()
    
    return int(line[0])

def synvalues():
    cmd = "/bin/netstat -an | grep 'SYN_RECV' | wc -l"
    #print cmd
    try :
        pipe = os.popen(cmd , "r" )
    except:
        print "can't system command exit"
        return 0
        
    line = pipe.readlines()
    pipe.close()
    
    return int(line[0])

def sysport():
    cmd = "nmap localhost"
    try:
        pipe = os.popen(cmd,"r")
    except:
        print "namp is not esxit"
    portfile = pipe.readlines()
    pipe.close()
    ports = []
    portstr = ''
    for line in portfile:
        b = line.strip("\n")
        portre = re.search('open',b)
        if portre is not None:
            port = re.findall(r'\d+',b)
            ports.append(port[0])
        else:
            continue
    for i in range(len(ports)):
        if i == 0:
            portstr = str(ports[i])
        else:
            portstr = portstr+","+str(ports[i])
            
    return portstr

if __name__ == "__main__":
    print '-------------------'
    networkinfo = []
    networkinfo = get_network_info()
    print networkinfo
    print '-------------------'
    print tcpvalues()
    print '-------------------'
    print synvalues()
    


