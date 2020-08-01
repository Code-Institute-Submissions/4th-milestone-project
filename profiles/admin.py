from django.contrib import admin
from .models import User, JobSeekerProfile, RecruiterProfile


class UserAdmin(admin.ModelAdmin):
    '''' Show user profile's fields in Admin'''
    list_display = (
        'username',
        'first_name',
        'last_name',
    )


admin.site.register(User, UserAdmin)
admin.site.register(JobSeekerProfile)
admin.site.register(RecruiterProfile)
