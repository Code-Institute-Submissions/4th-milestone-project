from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.login_success, name='profile'),
    path('candidate-profile/', views.candidate_profile, name='candidate_profile'),
    path('recruiter-profile/', views.recruiter_profile, name='recruiter_profile'),

]
