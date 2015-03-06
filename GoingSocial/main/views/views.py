from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from django import forms
from django.http import HttpResponseRedirect
from django.db import models

def splash(request):
	return render(request, 'main/splash.html',{})
	
def about(request):
    return render(request, 'main/about.html',{})

def home(request):
    return render(request, 'main/home.html',{})
	
def sign_up(request):
	return render(request,'main/sign_up.html',{})