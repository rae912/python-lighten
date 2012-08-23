#!/usr/bin/env python
########################################################################
#import
########################################################################
import os,sys
import logging
############## add custom model ###################
sys.path.append(".")
import linux.linuxinfo
import common.getconfig
########################################################################
rootpath = os.path.abspath(os.path.dirname(sys.argv[0]))
########################################################################
logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',
                    )
########################################################################
#main
########################################################################        
if __name__ == '__main__':
    logger = logging.getLogger('client')
    config = {}
    #config
    config = common.getconfig.read_config(rootpath)
    ip = common.getconfig.read_ip(rootpath)
    # Local arch
    logger.debug('Linux')
    #Linux info
    linuxobj = linux.linuxinfo.linux_info()
    #infosys
    linuxobj.init_info()
    #linuxinfo ip
    linuxobj.check_stat(ip)
    #config sys
    linuxobj.report_info(config)
    # Clean up
    a = open('/root/stat.txt','w')
    a.write('ok')
    a.close()
    logger.debug('done')
    sys.exit(0)
