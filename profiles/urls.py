from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.login_success, name='profile'),
    path('candidate-profile/', views.candidate_profile, name='candidate_profile'),
    #path('recruiter-profile/', views.recruiter_profile, name='recruiter_profile'),
    path('edit-candidate-profile/', views.edit_candidate_profile,
         name='edit_candidate_profile'),
    path('edit-work-experience/', views.edit_work_experience,
         name='edit_work_experience'),
    path('delete/<int:experience_id>/', views.delete_work_experience,
         name='delete_work_experience'),

]
