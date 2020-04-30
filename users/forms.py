from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ["username", "password"]

    def clean(self):
        if self.is_valid():
            if not authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password']):
                raise forms.ValidationError('Error, Invalid username or password!')

class AccountForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'photo', 'phone']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
