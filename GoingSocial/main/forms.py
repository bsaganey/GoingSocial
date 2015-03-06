from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import MyUser

date_widget =  {
            'birth': forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        }


class UserForm(UserCreationForm):
    model = User
    fields = ['username', 'password']


class MyUserForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ['email', 'name', 'hometown', 'city', 'birth', 'zipcode']