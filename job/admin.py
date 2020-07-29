from django.contrib import admin
from .models import Job, Author


class JobAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'author',
        'date_added',
        'last_modified',
    )

    ordering = ('date_added',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'user',
    )


admin.site.register(Job, JobAdmin)
admin.site.register(Author, AuthorAdmin)
