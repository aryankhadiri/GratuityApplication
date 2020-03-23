from .models import Employee
from django.forms import ModelForm
from django import forms


class EmployeeForm(forms.ModelForm):
    name = forms.CharField(max_length = 100)
    point = forms.FloatField()
    phone = forms.CharField(max_length = 10)
    class Meta:
        model = Employee
        fields = "__all__"