#!/usr/bin/env python
#-*- coding:utf-8 -*-

import MySQLdb
import MySQLdb.cursors


class TestMysql:
    def __init__(self):
        self.sql = ''
    def ConnectMysql(self,sql):
        try:
            conn = MySQLdb.connect(host="127.0.0.1",user="root",passwd="redhat",db='lighten',port=3306)
            cur = conn.cursor()
            cur.execute("""set names utf8""")
            cur.execute("""%s""" % (sql))
            cur.close()
            conn.close()
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0],e.args[1])
    def SelectMysql(self,select):
        try:
            conn = MySQLdb.connect(host="127.0.0.1",user="root",passwd="redhat",db='lighten',port=3306)
            cur = conn.cursor()
            cur.execute("""set names utf8""")
            cur.execute("""%s""" % (select))
            rows = cur.fetchall()
            cur.close()
            conn.close()
            return rows
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0],e.args[1])
    def DictMysql(self,dictsql):
	try:
	    conn = MySQLdb.connect(host="127.0.0.1",user="root",passwd="redhat",db='lighten',port=3306,charset='utf8',cursorclass=MySQLdb.cursors.ListCursor)
	    cur = conn.cursor()
	    cur.execute("""set names utf8""")
            cur.execute("""%s""" % (dictsql))
            rows = cur.fetchall()
            cur.close()
            conn.close()
            return rows
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0],e.args[1])
