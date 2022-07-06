from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class CustomRegisterForm(UserCreationForm):
    Store_Name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['Store_Name', 'username', 'email', 'password1', 'password2']
