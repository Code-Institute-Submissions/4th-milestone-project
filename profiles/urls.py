from django.urls import path
from . import views

urlpatterns = [
    path('myprofile', views.profile, name='profile'),

]
