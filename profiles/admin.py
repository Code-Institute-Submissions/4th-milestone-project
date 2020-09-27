from django.contrib import admin
from .models import User, JobSeekerProfile, RecruiterProfile


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
    )


class JobSeekerProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'preferred_job',
        'location',
    )


class RecruiterProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'position',
        'company_name',
        'company_city',
        'company_country',
    )


admin.site.register(User, UserAdmin)
admin.site.register(JobSeekerProfile, JobSeekerProfileAdmin)
admin.site.register(RecruiterProfile, RecruiterProfileAdmin)
