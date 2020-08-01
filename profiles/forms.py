from django import forms
from .models import User, JobSeekerProfile, RecruiterProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('profile_image', 'first_name', 'last_name', 'location',
                  'phone_number', 'email', 'job_title', 'about_me',)
        labels = {
            'profile_image': 'Profile image',
            'first_name': 'First name',
            'last_name': 'Last name',
            'location': 'Location',
            'phone_number': 'Phone number',
            'email': 'email',
            'job_title': 'Job title',
            'about_me': 'About me',
        }


class JobSeekerProfileForm(forms.ModelForm):
    class Meta:
        model = JobSeekerProfile
        fields = ('work_experience', 'education', 'languages',
                  'coding_languages',)
        labels = {
            'work_experience': 'Work experience',
            'education': 'Education',
            'languages': 'Languages',
            'coding_languages': 'Coding languages',
        }


class RecruiterProfileForm(forms.ModelForm):
    class Meta:
        model = RecruiterProfile
        fields = ('company_name', 'company_address1', 'company_address2',
                  'company_city', 'company_ZIP', 'company_state', 'company_country',)
        labels = {
            'company_name': 'Company name',
            'company_address1': 'Address',
            'company_address2': 'Apartment, suite etc.',
            'company_city': 'City',
            'company_ZIP': 'ZIP/Postal code',
            'company_state': 'State/Province',
            'company_country': 'Country/region',
        }
        widgets = {
            'company_address2': forms.TextInput(attrs={'placeholder': 'Example: 2nd floor'}),
        }
