from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django import forms

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email',]

class UpdateProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField()
    class Meta:
        model = Profile
        fields = ['profile_pic']