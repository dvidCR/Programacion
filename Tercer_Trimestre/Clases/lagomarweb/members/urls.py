from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('sign-in/', views.sign_in, name='sign-in'),
]