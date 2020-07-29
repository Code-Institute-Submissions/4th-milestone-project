from django.contrib import admin
from .models import Jobs


class JobsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'author',
        'date_added',
        'last_modified',
    )

    ordering = ('date_added',)


admin.site.register(Jobs, JobsAdmin)
