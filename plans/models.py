from django.db import models
from profiles.models import RecruiterProfile


PLAN_CHOICES = (
    ('Jobseeker plan', 'Jobseeker plan'),
    ('Recruiter plan', 'Recruiter plan')
)


class Plans(models.Model):
    plan_type = models.CharField(
        choices=PLAN_CHOICES,
        default='Jobseeker plan',
        max_length=50)
    price = models.IntegerField(default=25)
    stripe_pricing_id = models.CharField(max_length=50)

    def __str__(self):
        return self.plan_type


class PlanSubscription(models.Model):
    recruiter_profile = models.ForeignKey(
        RecruiterProfile, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.recruiter_profile.user.username
