from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.login_success, name='profile'),
    path('candidate-profile/', views.candidate_profile, name='candidate_profile'),
    path('recruiter-profile/', views.recruiter_profile, name='recruiter_profile'),
    path('recruiter-profile/edit-recruiter-profile/', views.edit_recruiter_profile,
         name='edit_recruiter_profile'),
    path('candidate-profile/edit-candidate-profile/', views.edit_candidate_profile,
         name='edit_candidate_profile'),
    path('candidate-profile/edit-work-experience/', views.edit_work_experience,
         name='edit_work_experience'),
    path('candidate-profile/edit-work-experience/delete/<int:experience_id>/', views.delete_work_experience,
         name='delete_work_experience'),
    path('candidate-profile/edit-education/', views.edit_education,
         name='edit_education'),
    path('candidate-profile/edit-education/delete/<int:education_id>/', views.delete_education,
         name='delete_education'),

]
