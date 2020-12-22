from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta :
        model = User
        fields = ['username','email','password1','password2']

class UserProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']
    
class ProfilePicUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

    