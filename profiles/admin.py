from django.contrib import admin
from .models import UserProfile, UserType


class UserProfileAdmin(admin.ModelAdmin):
    '''' Show user profile's fields in Admin'''
    list_display = (
        'user',
        'first_name',
        'last_name',
        'user_type',
    )


# Registering models to Admin
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserType)
