from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from okstupid.models import Profile

# Create your views here.

def register(request):
  auth.logout(request)
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    if password == password2:
      if User.objects.filter(username=username).exists():
        context = {'error': 'Impossible username input, please try again.'}
        return render(request, 'home.html', context)
      else:
        if User.objects.filter(email=email).exists():
          context = {'error': 'Impossible email input, please try again.'}
          return render(request, 'home.html', context)
        else:
          user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
            )
          user.save()
          user = auth.authenticate(username=username, password=password)
          if user is not None:
            auth.login(request, user)
            return redirect('create_profile')
          else:
            return redirect('login')
    else:
      context = {'error': 'Passwords do not match.'}
      return render(request, 'home.html', context)
  else:
    return render(request, 'register.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
      auth.login(request, user)
      return redirect('singles_list')
    else:
      context = {'error':'Invalid username or password'}
      return render(request, 'login.html', context)
  else:
    return render(request, 'login.html')


def logout(request):
  auth.logout(request)
  return redirect('home')