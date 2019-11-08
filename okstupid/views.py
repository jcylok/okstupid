from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile, Matched
from .forms import ProfileForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

def profile(request):
  profile = Profile.objects.get(user_id=request.user.id)
  context = {'profile':profile}
  return render(request, 'profile.html', context)

def profile_edit(request):
    profile = Profile.objects.get(user_id=request.user.id)
    print(profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    context = {'profile': profile, 'form': form, 'header': f"Edit profile: {profile.nickname}"}
    return render(request, 'profile_form.html', context)


def create_profile(request):
  print(request.user)
  if request.method == 'POST':
    form = ProfileForm(request.POST)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user_id = request.user
      profile.save()
      profile = Profile.objects.get(user_id=request.user.id)
      context = {'profile':profile}
      return render(request, 'profile.html', context)
  else:
    form = ProfileForm()
    context = {'form': form, 'header': 'Create Your Profile'}
    return render(request, 'profile_form.html', context)

def singles_list(request):
  profiles = Profile.objects.filter().exclude(user_id=request.user)
  context = {'profiles': profiles}
  return render(request, 'find_singles.html', context)


def profile_delete(request):
  User.objects.get().delete()
  return redirect('home')