from django.db import forms
from main.models import User

date_widget =  {
            'birth': forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'name', 'hometown', 'city', 'birth', 'zipcode']