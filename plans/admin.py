from django.contrib import admin
from .models import Plans, PlanSubscription


class PlansAdmin(admin.ModelAdmin):
    list_display = (
        'plan_type',
        'price',
        'stripe_pricing_id',
    )


class PlanSubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'recruiter_profile',
        'stripe_subscription_id',
        'active',
    )


admin.site.register(Plans, PlansAdmin)
admin.site.register(PlanSubscription, PlanSubscriptionAdmin)
