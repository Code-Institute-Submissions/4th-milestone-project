from django import forms
from .models import User, JobSeekerProfile, RecruiterProfile, WorkExperience


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('profile_image', 'first_name', 'last_name',
                  'phone_number', 'email', 'about_me',)
        labels = {
            'profile_image': 'Profile image',
            'first_name': 'First name',
            'last_name': 'Last name',
            'phone_number': 'Phone number',
            'email': 'E-mail',
            'about_me': 'About me',
        }


class JobSeekerProfileForm(forms.ModelForm):
    class Meta:
        model = JobSeekerProfile
        fields = ('location',)
        labels = {
            'location': 'Location',
            # 'education': 'Education',
            # 'languages': 'Languages',
            # 'coding_languages': 'Coding languages',
        }


class RecruiterProfileForm(forms.ModelForm):
    class Meta:
        model = RecruiterProfile
        fields = ('position', 'company_name', 'company_address1', 'company_address2',
                  'company_city', 'company_ZIP', 'company_state', 'company_country',)
        labels = {
            'position': 'Position',
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


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ('job_title', 'start_date', 'end_date',
                  )
        labels = {
            'job_title': 'Job title',
            'start_date': 'Start date',
            'end_date': 'End date',
        }
