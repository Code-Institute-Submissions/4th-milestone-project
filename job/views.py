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

@login_required
def edit_job(request, job_id):
    """ A view to edit a job profile """
    job = get_object_or_404(Job, pk=job_id)

    if request.user.id != job.author:
        return redirect(reverse('view_home'))
    
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect(reverse('job_profile', args=[job.id]))

    else:
        form = JobForm(instance=job)

    template = 'job/edit_job.html'
    context = {
        'title': 'Edit job profile',
        'form': form,
        'job': job,
    }

    return render(request, template, context)