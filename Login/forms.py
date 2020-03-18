from django import forms
from .models import User
from django.core.validators import EmailValidator

class LoginForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(), validators=[EmailValidator()])
    password = forms.PasswordInput()
    
    
    class Meta:
        model = User
        fields = {
            'email',
            'password'
        }