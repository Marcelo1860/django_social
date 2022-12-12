from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput)
    email = forms.EmailField()
    password1= forms.CharField(label='Password', widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_text = {k:"" for k in fields}