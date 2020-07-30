from django.db import models
from django.contrib.auth.models import User


class UserType(models.Model):
    USER_TYPE_CHOICES = (
        'Job seeker', 'Job seeker'), ('Recruiter', 'Recruiter')
    user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=10)

    def __str__(self):
        return self.user_type


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_type = models.ForeignKey(
        UserType, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username
