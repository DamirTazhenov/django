from django.shortcuts import render, HttpResponseRedirect
from .forms import UserLoginForm, UserRegisterForm
from django.contrib import auth
from django.urls import reverse

def login(request):
    if request.method =="POST":
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse(''))
    else:
        form = UserLoginForm()
    context = {
        'form': UserLoginForm(),
    }
    return render(request, 'users/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()
    context = {
        "form": UserRegisterForm(),
    }
    return render(request, 'users/register.html', context)
# Create your views here.
