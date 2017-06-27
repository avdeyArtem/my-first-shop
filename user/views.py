from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators import csrf
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login as auth_login, logout
# Create your views here.
def register(request):
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/')
            return HttpResponseRedirect('/')

    else:
        form = RegistrationForm()
        context = {'form':form}

    return render(request, "catalog/reg.html", context)

def login(request):
    context = {}
    username = password = ''
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/')
    return render(request, "catalog/reg.html", context)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
