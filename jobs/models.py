from django.db import models
from profiles.models import User


class Jobs(models.Model):
    class Meta:
        verbose_name_plural = 'Jobs'

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1024)
    # Delete job when user is deleted
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    # Date is created when job is created and can't be modified
    date_added = models.DateTimeField(
        auto_now_add=True, editable=False, blank=True)
    # Date is created when job is modified and can't be modified
    last_modified = models.DateTimeField(
        auto_now=True, editable=False, blank=True)

    def __str__(self):
        return self.title
