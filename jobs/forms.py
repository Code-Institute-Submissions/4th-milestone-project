from django import forms
from .models import Jobs


class JobsForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ('title', 'description', 'languages',
                  'coding_languages', 'frameworks')


class SearchForm(forms.Form):
    description = forms.CharField()
