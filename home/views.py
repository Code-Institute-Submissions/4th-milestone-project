from django.shortcuts import render
from profiles.models import User
from jobs.models import Jobs


def view_home(request):
    """ A view to return the index page """

    user_count = User.objects.all().count()
    candidate_count = User.objects.filter(is_job_seeker=True).count()
    recruiter_count = User.objects.filter(is_job_seeker=False).count()
    job_count = Jobs.objects.all().count()
    recent_jobs = Jobs.objects.order_by('-date_added')[:5]

    template = 'home/index.html'
    context = {
        'user_count': user_count,
        'job_count': job_count,
        'candidate_count': candidate_count,
        'recruiter_count': recruiter_count,
        'recent_job_list': recent_jobs,
    }

    return render(request, template, context)
