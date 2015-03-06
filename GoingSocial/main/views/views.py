from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import  authenticate, login, logout
from django.contrib.auth.models import User
from main.models import MyUser
from main.forms import UserForm, MyUserForm, SignInForm

def home(request):
    request.session['name'] = 'Ludwik'
    return render(request, 'home.html', {})


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
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
        user_form = UserForm(request.POST)
        myuser_form = MyUserForm(request.POST)
        if all((user_form.is_valid(), myuser_form.is_valid())):
            new_user = user_form.save()
            new_myuser = myuser_form.save(commit=False)
            new_myuser.user = new_user
            new_myuser.save()
            return HttpResponseRedirect('/thanks')
    else:
        user_form = UserForm()
        myuser_form = MyUserForm()
    return render(request, 'main/sign_up.html', {'user_form': user_form, 'myuser_form': myuser_form})

def splash(request):
	return render(request, 'main/splash.html',{})
	
def about(request):
    return render(request, 'main/about.html', {'moo': request.session['name']})
