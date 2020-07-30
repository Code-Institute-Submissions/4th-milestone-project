from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import JobsForm
from .models import Jobs
from profiles.models import UserProfile
from profiles.utils import get_profile


def all_jobs(request):
    """ A view to return the job page """
    template = 'jobs/job.html'

    return render(request, template)


@login_required
def add_job(request):
    """ A view to add a new job """
    form = JobsForm(request.GET)
    author = get_profile(request.user)

    if request.method == 'POST':
        form = JobsForm(request.POST)
        if form.is_valid():
            form.instance.author = author
            form.save()
            messages.success(request, 'You have successfully added a new job!')
            return redirect(reverse('all_jobs'))
        else:
            messages.error(request,
                           ('Could not add the new job. '
                            'Make sure you entered valid data.'))
    # Empty form instantiation in order to make Bootstrap error messages working correctly
    else:
        form = JobsForm()

    template = 'jobs/add_job.html'
    context = {
        'title': 'Add new job',
        'form': form,
    }

    return render(request, template, context)


def job_profile(request, job_id):
    """ A view to show job profile """

    job = get_object_or_404(Jobs, pk=job_id)

    template = 'jobs/job_profile.html'
    context = {
        'title': 'Job profile',
        'job': job,
    }

    return render(request, template, context)


@login_required
def edit_job(request, job_id):
    """ A view to edit a job profile """
    job = get_object_or_404(Jobs, pk=job_id)

    if request.user.id != job.author.id:
        messages.error(request, 'You can only edit your own job profiles')
        return redirect(reverse('view_home'))

    if request.method == 'POST':
        form = JobsForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'You have successfully updated the job profile!')
            return redirect(reverse('job_profile', args=[job.id]))
        else:
            messages.error(request,
                           ('Could not update job profile. '
                            'Make sure you entered valid data.'))
    else:
        form = JobsForm(instance=job)
        messages.info(request, f'You are editing {job.title}')

    template = 'jobs/edit_job.html'
    context = {
        'title': 'Edit job profile',
        'form': form,
        'job': job,
    }

    return render(request, template, context)


@login_required
def delete_job(request, job_id):
    """ A view to delete a job profile """
    job = get_object_or_404(Jobs, pk=job_id)

    if request.user.id != job.author.id:
        messages.error(request, 'You can only delete your own job profiles')
        return redirect(reverse('view_home'))

    job.delete()
    messages.success(request, 'You have successfully deleted the job profile!')
    return redirect(reverse('all_jobs'))
