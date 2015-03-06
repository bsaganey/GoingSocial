from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from django import forms
from django.http import HttpResponseRedirect
from django.db import models



def signup_form(request):
    if request.method == 'POST':
        form = UserlForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/moo')
    else:
        form = UserForm()
    return render(request, 'main/signup.html', {'form': form})

def splash(request):
	return render(request, 'main/splash.html',{})
	
def about(request):
	return render(request, 'main/about.html',{})
	
def SignUp(request):
	return render(request,'main/SignUp.html',{})



