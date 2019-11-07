from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
# from django.contrib.auth.decorators import login_required

from .models import Profile, Matched

# Create your views here.

def home(request):
    return render(request, 'home.html')
<<<<<<< HEAD
=======

>>>>>>> 511a52034d8728fcbfefdd8234070d14502df85e

def profile(request):
  profiles = Profile.objects.filter(user=request.user)
  context = {'profiles':profiles}
  return render(request, 'profile.html', context)
<<<<<<< HEAD
=======

>>>>>>> 511a52034d8728fcbfefdd8234070d14502df85e
