from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from okstupid.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 

# Create your views here.

def register(request):
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    if password == password2:
      # check if username exits in db
      if User.objects.filter(username=username).exists():
        context = {'error': 'Username is already taken.'}
        return render(request, 'register.html', context)
      else:
        if User.objects.filter(email=email).exists():
          context = {'error': 'Username is already taken.'}
          return render(request, 'register.html', context)
        else:
          #if everything is ok create account
          user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name)
          user.save()
          return redirect('login')
    else:
      context = {'error': 'Password do not match'}
      return render(request, 'register.html', context)
  else:
    # if not post send form
    return render(request, 'register.html')
        

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
      auth.login(request, user)
      return redirect('profile')
    else:
      context = {'error':'Invalid username or password'}
      return render(request, 'login', context)
  else:
    return render(request, 'login.html')


def logout(request):
  auth.logout(request)
  return redirect('home')