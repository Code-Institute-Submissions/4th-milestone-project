from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'user_type',)
        labels = {
            "first_name": "First name",
            "last_name": "Last name",
            "user_type": "Which user type fits you best?",

        }
