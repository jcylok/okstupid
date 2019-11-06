from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('profile/<int:pk>/', views.profile_show, name='profile_show'),
  path('profile/<int:pk>/edit', views.profile_edit, name='profile_edit'),
  path('profile/<int:pk>/delete', views.profile_delete, name='profile_delete'),

  path('profile/<int:pk>/findsinlges', views.profile_findsingles, name='profile_findsingles'),
  path('profile/<int:pk>/matches', views.profile_matches, name='profile_matches'),

  path('connected/<int:match_id>', views.profile_connected, name='profile_connected')

]