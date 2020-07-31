from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    location = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=15)
    job_title = models.CharField(max_length=50)
    about_me = models.TextField(max_length=500)
    is_job_seeker = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class JobSeekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    work_experience = models.TextField(max_length=500)
    education = models.TextField(max_length=500)
    languages = models.TextField(max_length=500)
    coding_languages = models.TextField(max_length=500)


class RecruiterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    company_address1 = models.CharField(max_length=50)
    company_address2 = models.CharField(max_length=50, blank=True)
    company_city = models.CharField(max_length=50)
    company_ZIP = models.CharField(max_length=50, blank=True)
    company_state = models.CharField(max_length=50)
    company_country = models.CharField(max_length=50)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if instance.is_job_seeker:
        JobSeekerProfile.objects.get_or_create(user=instance)
    else:
        RecruiterProfile.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_job_seeker:
        instance.jobseekerprofile.save()
    else:
        instance.recruiterprofile.save()
