from .models import User


def get_profile(user):
    return User.objects.filter(user=user).first()
