from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
# from django.contrib.auth.decorators import login_required

from .models import Profile, Matched

# Create your views here.

def home(request):
    return render(request, 'home.html')

