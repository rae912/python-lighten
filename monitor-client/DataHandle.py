#!/usr/bin/env python
#-*- coding:utf-8 -*-

class StrCom:
    def __init__(self):
        str = ''
        connstr = ''
        end = ''
    def strHandle(self,str,connstr):
        connstr = connstr[0]
        str.remove(str[0])
        if len(str) == len(connstr):
            end = len(str) - 1
            for i in range(len(str)):
                if str[i] == connstr[i]:
                    if i == end:
                        return True
                        break
                    else:
                        continue
                else:
                    return False
                    break
        else:
            return False

    def ListHandle(self,str,connstr):
        connstr = connstr[0]
        if len(str) == len(connstr):
            end = len(str) - 1
            for i in range(len(str)):
		if i == 0:
		    continue
                elif str[i] == connstr[i]:
                    if i == end:
                        return True
                        break
                    else:
                        continue
                else:
                    return False
                    break
        else:
            return False
