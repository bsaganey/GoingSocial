from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.models import User
from main.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def home(request):
    #request.session['name'] = 'Ludwik'
    return render(request, 'home.html', {})


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email = email, password = password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'Incorrect email or password')
                return HttpResponseRedirect('/sign_in/')
    elif request.method == 'GET':
        form = SignInForm()
    else:
        return HttpResponseRedirect('/sign_in/')
    return render(request, "sign_in.html", {"form": form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


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
    return render(request, 'main/about.html', {'moo': request.session['name']})