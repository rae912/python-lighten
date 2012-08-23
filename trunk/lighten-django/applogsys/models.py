from django.db import models

class ServerLog(models.Model):
    mac_addr =  models.CharField(max_length=50, primary_key=True)
    domain_name = models.CharField(max_length=30)
    flow_rate = models.CharField(max_length=30)
    browse = models.IntegerField(20)
    err500 = models.CharField(max_length=10)
    err504 = models.CharField(max_length=10)
    err302 = models.CharField(max_length=10)
    err404 = models.CharField(max_length=10)

class LoginLog(models.Model):
    mac_addr =  models.CharField(max_length=50, primary_key=True)
    source_host_macaddr = models.CharField(max_length=30)
    target_host_macaddr = models.CHarField(max_length=30)
    access_user = models.CHarField(max_length=30)
    login_time = models.CHarField(max_length=30)
    loginout_time = models.CHarField(max_length=30)

class FaultLog(models.Model):
    fault_ip_mac = models.CharField(max_length=50, primary_key=True)
    fault_time = models.CHarField(max_length=30)
    fault_recovery_time = models.CHarField(max_length=30)
    fault_reason = models.CHarField(max_length=50)
