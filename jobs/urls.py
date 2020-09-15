from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_jobs, name='all_jobs'),
    path('search/', views.search, name='search'),
    path('add/', views.add_job, name='add_job'),
    path('edit/<int:job_id>/', views.edit_job, name='edit_job'),
    path('delete/<int:job_id>/', views.delete_job, name='delete_job'),
    path('profile/<int:job_id>/', views.job_profile, name='job_profile'),
]
