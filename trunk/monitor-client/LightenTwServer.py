#!/usr/bin/env python
#-*- coding:utf-8 -*-

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
from Mysqlhandle import MysqlHandle
import time

#定义参数
PORT = 8081
Nowtime = time.strftime("%Y-%m-%d %H:%M:%S")


class TSServProtocol(Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print "连接服务器IP：%s" % clnt

    def dataReceived(self, data):
        sql = MysqlHandle()
        sql.DataHandle(data)    #处理数据，将数据保存到数据库
        #self.transport.write("ok")    #如果保存成功给客户端返回一个状态

if __name__ == '__main__':
    #实例化Factory
    factory = Factory()
    factory.protocol = TSServProtocol
    #监听指定的端口
    reactor.listenTCP(PORT,factory)
    #开始运行主程序
    reactor.run()
