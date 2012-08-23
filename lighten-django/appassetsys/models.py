#-*- coding:utf-8 -*-
from django.db import models
# Create your models here.
class Hdinfo(models.Model):
    SerialNum=models.CharField(u'序列号',max_length=50,primary_key=True)
    ModelNum=models.CharField(u'型号',max_length=50)
    Cpu=models.CharField(u'CPU型号',max_length=50)
    Memory=models.CharField(u'内存大小',max_length=10)
    MemNum=models.IntegerField(u'内存数量',max_length=3)
    Hdisk=models.CharField(u'硬盘大小',max_length=10)
    HdNum=models.IntegerField(u'硬盘数量',max_length=3)
    InternalNum=models.CharField(u'内部编号',max_length=50)
    DatePurchese=models.DateField(u'购买日期')
    def __unicode__(self):
        return self.ModelNum
class Blinfo(models.Model):
    """
    # jj
    >>> myuser = Blinfo.objects.create(SerialNum='CNUW423ES1',Department='boss',Competent='admin',CabinetNum='23-9884',Purpose='test HPC',AddTime='2012-7-22')
    >>> myuser.SerialNum
    'CNUW423ES10'
    """
    SerialNum=models.CharField(u'序列号',max_length=50,primary_key=True)
    Department=models.CharField(u'部门',max_length=20)
    Competent=models.CharField(u'负责人',max_length=50)
    CabinetNum=models.CharField(u'机柜编号',max_length=50)
    Purpose=models.TextField(u'用途',max_length=500)
    AddTime=models.DateField(u'上架时间',)
    def __unicode__(self):
        return self.SerialNum
