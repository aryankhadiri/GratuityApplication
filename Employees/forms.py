from django import forms
from .models import Form
from .models import Tip
from datetime import datetime

class TipForm(forms.ModelForm):
    date = forms.DateField(widget=forms.HiddenInput(attrs = {
        'class': 'Date',
        'id': 'TFdate'
        

        
    }))

    employee = forms.Select(attrs={
        'class': 'name',
    }) 
    time_frame = forms.Select(attrs = {
        'class': 'time_frame',
        'id': 'time_frame'
    })    
    point = forms.FloatField(widget = forms.NumberInput(attrs = {
        'class': 'point'
    }))
    tip_amount = forms.FloatField(widget = forms.NumberInput(attrs={
        'class': 'tip'
    }))
    paid_today = forms.FloatField(widget = forms.NumberInput(attrs={
        'class': 'paid_today'
    }))
    point = forms.FloatField(widget = forms.NumberInput(attrs={
        'class': 'performance_index'
    }))
    
    paid_later = forms.FloatField(widget = forms.NumberInput(attrs={
        'class': 'paid_later'
    }))
    class Meta:
        model = Tip
        fields = {
            'date',
            'employee',
            'point',
            'tip_amount',
            'paid_later',
            'time_frame',
            'paid_today'
        }
class newForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs = {
        'class': 'Date',
        'id': 'NFdate',
        'onblur':"copyDate()",
        'value':datetime.now().date()

        
    }))
    time_frame = forms.Select(attrs = {
        'class': 'time_frame',
        'id': 'time_frame'
    })
    
    submitted_employee = forms.Select(attrs={
        'class':'submitted_employee',
        'id':'submitted_employee'
    })
    cc_tip = forms.FloatField(widget = forms.NumberInput(attrs = {
        'class': 'cc_tip',
        'id': 'cc_tip',
    }))
    service_charge = forms.FloatField(widget = forms.NumberInput(attrs={
        'class': 'service_charge',
        'id': 'service_charge'
    }))
    cash_sales = forms.FloatField(widget = forms.NumberInput(attrs={
        'class': 'cash_sales',
        'id': 'cash_sales'

    }))
    cash_tip = forms.FloatField(widget = forms.NumberInput(attrs={
        'class': 'cash_tip',
        'id': 'cash_tip'
    }))
    pre_shift_tip = forms.FloatField(widget = forms.NumberInput(attrs={
        'class': 'pre_shift_tip',
        'id': 'pre_shift_tip'
    }))
    time = forms.TimeField(widget= forms.HiddenInput(attrs={
        'value':datetime.now().time()
    }))
    class Meta:
        model = Form
        fields = {
            'date',
            'time_frame',
            'submitted_employee',
            'cc_tip',
            'service_charge',
            'cash_sales',
            'cash_tip',
            'pre_shift_tip',
            'time'
        }
    #def __init__(self, time):
