#-*- coding:utf8 -*-
from django import forms
from models import Hdinfo
from models import Blinfo
class HdinfoForm(forms.ModelForm):
    class Meta:
        model = Hdinfo
        fields = ('SerialNum','ModelNum','Cpu','Memory','MemNum','Hdisk','HdNum','InternalNum','DatePurchese')

class BlinfoForm(forms.ModelForm):
    class Meta:
        model = Blinfo
        fields = ('SerialNum','Department','Competent','CabinetNum','Purpose','AddTime')
