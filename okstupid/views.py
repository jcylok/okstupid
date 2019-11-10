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
    context = {'profile': profile, 'form': form, 'header': f"{profile.user_id.first_name}, make sure to save the changes!"}
    return render(request, 'profile_form.html', context)


def create_profile(request):
  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user_id = request.user
      profile.photo_one = request.FILES["photo_one"]
      profile.save()
      profile = Profile.objects.get(user_id=request.user.id)
      return redirect('singles_list')
  else:
    form = ProfileForm()
    context = {'form': form, 'header': 'Create Your Profile'}
    return render(request, 'profile_form.html', context)

def singles_list(request):
  myprofile = Profile.objects.get(user_id=request.user)
  profiles = Profile.objects.filter(
    age__lte=myprofile.age_preference_max,
    age__gte=myprofile.age_preference_min,
    gender=myprofile.gender_preference
    ).exclude(user_id=request.user)
  context = {'profiles': profiles}
  return render(request, 'find_singles.html', context)

def profile_show(request, pk):
  profile = Profile.objects.get(id=pk)
  target_id = Profile.objects.get(id=pk).user_id
  pair = None
  if Matched.objects.filter(profile_id_init=target_id, profile_id_connect=request.user).exists():
    pair = Matched.objects.get(profile_id_init=target_id, profile_id_connect=request.user)
  if Matched.objects.filter(profile_id_init=request.user, profile_id_connect=target_id).exists():
    pair = Matched.objects.get(profile_id_init=request.user, profile_id_connect=target_id)
  print(pair)
  context = {'profile': profile, 'pair': pair }
  return render(request, 'profile.html', context)

def profile_delete(request, pk):
  User.objects.get(id=pk).delete()
  return render(request, 'home.html', {'pk': pk})

def match_handle(request, pk):
  my_id = request.user
  target_id = Profile.objects.get(id=pk).user_id
  if Matched.objects.filter(profile_id_init=my_id, profile_id_connect=target_id).exists() or Matched.objects.filter(profile_id_init=target_id, profile_id_connect=my_id).exists():
    if Matched.objects.filter(profile_id_init=my_id, profile_id_connect=target_id).exists():
      t = Matched.objects.filter(profile_id_init=my_id, profile_id_connect=target_id)
      t.update(confirmed=True)
    elif Matched.objects.filter(profile_id_init=target_id, profile_id_connect=my_id).exists():
      t = Matched.objects.filter(profile_id_init=target_id, profile_id_connect=my_id)
      t.update(confirmed=True)
    return redirect('singles_list')
  else:
    pair = Matched(profile_id_init=my_id, profile_id_connect=target_id)
    pair.save()
    return redirect('singles_list')

def matches_list(request):
  myprofile = Profile.objects.get(user_id=request.user)
  connections = Matched.objects.filter(profile_id_init=myprofile.user_id, confirmed=True) | Matched.objects.filter(profile_id_connect=myprofile.user_id, confirmed=True)
  myloves = []
  for connection in connections:
    if connection.profile_id_init != request.user:
      myloves.append(connection.profile_id_init)
    if connection.profile_id_connect != request.user:
      myloves.append(connection.profile_id_connect)
  myloves_profiles = Profile.objects.filter(user_id__in = myloves)
  context = {'myprofile': myprofile, 'myloves_profiles': myloves_profiles }
  return render(request, 'matches.html', context)
