from django.db import models
#-*- coding:utf-8 -*-

# Create your models here.
class hosts_info(models.Model):
    mac = models.CharField(max_length=20, primary_key=True)
    ip = models.CharField(max_length=20)
    idc = models.CharField(max_length=15)
    infosys = models.CharField(max_length=75)

class cpu_info(models.Model):
    mac = models.CharField(max_length=20, primary_key=True)
    mname = models.CharField(max_length=100)
    mcores = models.CharField(max_length=15)
    mclockspeed = models.CharField(max_length=20)
    ip = models.ForeignKey(hosts_info)

class disk_info(models.Model):
    mac = models.CharField(max_length=20)
    mcaption = models.CharField(max_length=20)
    mfs_name = models.CharField(max_length=20)
    mfs_size = models.CharField(max_length=20)
    mfs_free = models.CharField(max_length=20)
    mfs_use = models.CharField(max_length=20)
    mfs_used = models.CharField(max_length=15)
    ip = models.ForeignKey(hosts_info)

class network_info(models.Model):
    mac = models.CharField(max_length=20, primary_key=True)
    mname = models.CharField(max_length=20)
    mmask = models.CharField(max_length=20)
    mmtu = models.CharField(max_length=10)
    mdrive = models.CharField(max_length=20)
    mmodel = models.CharField(max_length=20)
    ip = models.ForeignKey(hosts_info)

class ipnet_info(models.Model):
    ipnet = models.CharField(max_length=20, primary_key=True)
    netname = models.CharField(max_length=20)
