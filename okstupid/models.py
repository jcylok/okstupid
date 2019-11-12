from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.core.validators import MinLengthValidator
from django.utils.text import slugify




fs = FileSystemStorage(location='/media/photos')

# Create your models here.
class Profile(models.Model):
  nickname = models.CharField(max_length=15, validators=[MinLengthValidator(2)])
  gender = models.CharField(blank=True,max_length=5)
  age = models.PositiveIntegerField()
  height = models.CharField(max_length=5)
  location = models.CharField(max_length=25)
  job_title = models.CharField(max_length=25)
  education = models.CharField(max_length=50)
  hometown = models.CharField(max_length=25)
  drinker = models.BooleanField(default=False)
  smoker = models.BooleanField(default=False)
  photo_one = models.ImageField(upload_to='photos', blank=True)
  photo_two = models.ImageField(upload_to='photos', blank=True)
  photo_three = models.ImageField(upload_to='photos', blank=True) 
  prompt_one = models.CharField(max_length=255)
  prompt_two = models.CharField(max_length=255)
  prompt_three = models.CharField(max_length=255)
  age_preference_max = models.PositiveIntegerField()
  age_preference_min = models.PositiveIntegerField()
  gender_preference = models.CharField(blank=True, max_length=25)
  slug = models.SlugField(unique=True)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles')
  def __str__(self):
    return self.nickname

  def save(self, *args, **kwargs):
    full_name = self.user_id.first_name + self.user_id.last_name + self.user_id.username
    self.slug = slugify(full_name)
    super(Profile, self).save(*args, **kwargs)


class Matched(models.Model):
  profile_id_init = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
  profile_id_connect = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever')
  confirmed = models.BooleanField(default=False)
  passed = models.BooleanField(default=False)

  def __str__(self):
    return f"{self.profile_id_init} - {self.profile_id_connect} - {self.confirmed}"



class Post(models.Model):
    author1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author1')
    author2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author2')

    def __str__(self):
        return f"{self.author1}-{self.author2}"

class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return {self.post}