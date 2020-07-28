from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_jobs, name='all_jobs'),
    path('add/', views.add_job, name='add_job'),
]