from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.models import User
from main.forms import UserForm

def home(request):
    return render(request, 'home.html', {})
    
def thanks(request):
	return render(request, 'thanks.html',{})

def sign_up(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks')
    else:
        form = UserForm()
    return render(request, 'main/sign_up.html', {'form': form})


def splash(request):
	return render(request, 'main/splash.html',{})
	
def about(request):
    return render(request, 'main/about.html',{})

def home(request):
    return render(request, 'main/home.html',{})