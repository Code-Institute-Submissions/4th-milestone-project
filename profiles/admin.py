from django.contrib import admin
from .models import User, JobSeekerProfile, RecruiterProfile


class GenericProfileAdmin(admin.ModelAdmin):
    '''' Show user profile's fields in Admin'''
    list_display = (
        'username',
        'first_name',
        'last_name',
    )


admin.site.register(User, GenericProfileAdmin)
admin.site.register(JobSeekerProfile)
admin.site.register(RecruiterProfile)
