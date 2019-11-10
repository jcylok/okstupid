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


def profile_form(request):
  if request.method == 'POST':
    nickname = request.POST['nickname']
    gender = request.POST['gender']
    age = request.POST['age']
    height = request.POST['height']
    location = request.POST['location']
    job_title = request.POST['job_title']
    education = request.POST['education']
    hometown = request.POST['hometown']
    drinker = request.POST['drinker']
    smoker = request.POST['smoker']
    photo_one = request.POST['photo_one']
    photo_two = request.POST['photo_two']
    photo_three = request.POST['photo_three']
    prompt_one = request.POST['prompt_one']
    prompt_two = request.POST['prompt_two']
    prompt_three = request.POST['prompt_three']
    age_preference_max = request.POST['age_preference_max']
    age_preference_min = request.POST['age_preference_min']
    gender_preference = request.POST['gender_preference']