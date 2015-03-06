from django import forms
from main.models import User

date_widget =  {
            'birth': forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        }


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