from django.urls import path
from . import views

urlpatterns = [
    path('job/', views.view_job, name='view_job')
]