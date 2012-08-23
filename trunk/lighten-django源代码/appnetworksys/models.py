# coding:utf-8
from django.db import models
from lighten.appinfosys.models import hosts_info


class ServerStatus(models.Model):
    
    mac = models.CharField(max_length=50)
    service_name = models.CharField(max_length=30)
    service_port = models.CharField(max_length=20)
    service_pid = models.CharField(max_length=20)
    service_status = models.CharField(max_length=10)
    ip = models.ForeignKey(hosts_info)


class Connections(models.Model):

    mac = models.CharField(max_length=50, primary_key=True)
    connections = models.CharField(max_length=20)  # 连接这台服务器的ip的数量
    ports = models.CharField(max_length=50)   # 端口号
    ip = models.ForeignKey(hosts_info)



