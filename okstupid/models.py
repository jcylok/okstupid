from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/media/photos')

# Create your models here.
class Profile():
  nickname = models.CharField(max_length=25, min_length=2)
  gender = models.CharField(blank=True)
  age = models.PositiveIntegerField(max_length=2, min_length=2)
  height = models.CharField(max_length=5)
  location = models.CharField(max_length=25)
  job_title = models.CharField(max_length=25)
  education = models.CharField(max_length=25)
  hometown = models.CharField(max_length=25)
  drinker = models.BooleanField(defaut=False)
  smoker = models.BooleanField(default=False)
  photo_one = models.ImageField(storage=fs, blank=True)
  photo_two = models.ImageField(storage=fs, blank=True)
  photo_three = models.ImageField(storage=fs, blank=True) 
  prompt_one = models.CharField(max_length=255)
  prompt_two = models.CharField(max_length=255)
  prompt_three = models.CharField(max_length=255)
  age_preference_max = models.PositiveIntegerField(max_length=2)
  age_preference_min = models.PositiveIntegerField(max_length=2)
  gender_preference = models.CharField(blank=True)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles')

class Matched():
  profile_id_init = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
  profile_id_connect = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever')
  confirmed = models.BooleanField(default=False)
