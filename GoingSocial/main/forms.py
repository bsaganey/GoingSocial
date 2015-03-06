from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import MyUser

date_widget =  {
            'birth': forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        }


<<<<<<< HEAD
class UserForm(UserCreationForm):
    model = User
    fields = ['username', 'password']


class MyUserForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ['email', 'name', 'hometown', 'city', 'birth', 'zipcode']
=======
class UserForm(forms.ModelForm):
    
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'name', 'hometown', 'city', 'birth', 'zipcode']
        widgets = {
            'password': forms.PasswordInput(),
        }

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
>>>>>>> 63f77db2734457c68d83ba5c72fc8fe4b14dbfa6
