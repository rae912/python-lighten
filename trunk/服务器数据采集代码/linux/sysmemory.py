#!/usr/bin/env python


def get_memory_info() :
    proc_path = "/proc/meminfo"
    try :
        f = open( proc_path, "r" )
        f.readlines()
        f.seek(0)
    except:
        print "Error:%s" % ( proc_path )
        return {}

    tmpdict = {}
    for line in f.readlines() :
        tmplist = line.split();
        tmpdict[tmplist[0]] = int(tmplist[1])
    f.close()
    retdict = {"MemTotal" : long(tmpdict["MemTotal:"])/1024, \
            "MemFree" : long(tmpdict["MemFree:"])/1024, \
            "SwapTotal" : long(tmpdict["SwapTotal:"])/1024, \
            "SwapFree" : long(tmpdict["SwapFree:"])/1024}
    return retdict

if __name__ == "__main__":
    print get_memory_info()
