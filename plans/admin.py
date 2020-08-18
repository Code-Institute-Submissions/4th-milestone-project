from django.contrib import admin
from .models import Plans, PlanSubscription

# Register your models here.
admin.site.register(Plans)
admin.site.register(PlanSubscription)
