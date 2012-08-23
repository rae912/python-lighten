#!/usr/bin/env python
import re,random


def reconfig(file):
    r = open(file)
    afile = r.read()
    num = random.randint(0,60)
    refile = re.sub('cnum',num,afile)
    r.close()
    refile1 = open(file,'wb')
    refile1.write(refile)
    refile1.close()
