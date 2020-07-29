from .models import UserProfile


def get_profile(user):
    return UserProfile.objects.filter(user=user).first()
