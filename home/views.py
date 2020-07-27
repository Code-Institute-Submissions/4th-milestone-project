from django.shortcuts import render


def view_home(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')