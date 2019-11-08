from django.urls import path
from django.contrib.auth.models import User
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.home, name='home'),

  path('profile/', views.profile, name='profile'),
  path('profile/edit', views.profile_edit, name='profile_edit'),
  path('profile/create', views.create_profile, name='create_profile'),
  path('profile/singles', views.singles_list, name='singles_list'),
  path('profile/delete', views.profile_delete, name='profile_delete')
  # path('profile/delete', views.profile_delete, name='profile_delete'),

  # path('profile/<int:pk>/', views.profile_show, name='profile_show'),
  # path('profile/matches', views.matches, name='matches'),

  # path('connected/<int:match_id>', views.profile_connected, name='profile_connected')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)