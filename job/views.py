from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import JobForm
from .models import Job, Author
from .utils import get_author


def all_jobs(request):
    """ A view to return the job page """
    template = 'job/job.html'

    return render(request, template)

@login_required
def add_job(request):
    """ A view to add a new job """
    form = JobForm(request.GET)
    author = get_author(request.user)

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('all_jobs'))
    # Empty form instantiation in order to make error messages working correctly
    else: 
        form = JobForm()

    template = 'job/add_job.html'
    context = {
        'title': 'Add new job',
        'form': form,
    }

    return render(request, template, context)

def job_profile(request, job_id):
    """ A view to show job profile """

    job = get_object_or_404(Job, pk=job_id)

    template = 'job/job_profile.html'
    context = {
        'title': 'Job profile',
        'job': job,
    }

    return render(request, template, context)