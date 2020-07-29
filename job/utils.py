from .models import Author

def get_author(user):
    return Author.objects.filter(user=user).first()