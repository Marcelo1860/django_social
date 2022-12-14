from cProfile import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput)
    email = forms.EmailField()
    password1= forms.CharField(label='Password', widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_text = {k:"" for k in fields}

class PostForm(forms.ModelForm):
    content = forms.CharField(label ='', widget = forms.Textarea(attrs={'rows':2,'placeholder':'Tell us something'}),required = True)

    class Meta:
        model = Post
        fields = ['content']

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput)
    class Meta:
        model = User
        fields = ['username']

class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Profile
        fields = ['image']