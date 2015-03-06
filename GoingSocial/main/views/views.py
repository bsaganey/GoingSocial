from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import  authenticate, login, logout
from django.contrib.auth.models import User
from main.models import MyUser
from main.forms import UserForm, MyUserForm, SignInForm


def sign_in(request):
    if request.method == 'POST':
        sign_in_form = SignInForm(request.POST)
        if sign_in_form.is_valid():
            username = sign_in_form.cleaned_data["username"]
            password = sign_in_form.cleaned_data["password"]
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponseRedirect('/sign_in/')
    elif request.method == 'GET':
        sign_in_form = SignInForm()
    else:
        return HttpResponseRedirect('/sign_in/')
    return render(request, "sign_in.html", {"sign_in_form": sign_in_form})


def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/home/')


def thanks(request):
	return render(request, 'thanks.html',{})


def sign_up(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    elif request.method == 'POST':
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
    return render(request, 'main/sign_up.html', 
        {'user_form': user_form, 'myuser_form': myuser_form})


def splash(request):
	return render(request, 'main/splash.html', {})


def home(request):
    return render(request, 'main/home.html', {})


def about(request):
    return render(request, 'main/about.html', {})


def profile(request, id):
    if request.user.is_authenticated():
        return render(request, "profile.html", 
            {'user': User.objects.get(id=id), 'myuser': MyUser.objects.get(user=id)})
    else:
        return HttpResponseRedirect('/splash/')

def blog(request):
    if request.user.is_authenticated():
        return render(request, "blog.html", 
            {'myuser': MyUser.objects.get(user=request.user.id)})
    else:
        return HttpResponseRedirect('/splash/')