from django.shortcuts import render


def view_job(request):
    """ A view to return the job page """

    return render(request, 'job/job.html')