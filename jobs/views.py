from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import JobsForm, SearchForm
from .models import Jobs
from profiles.models import RecruiterProfile
from django.db.models import Q


def all_jobs(request):
    """ A view to return the page with all jobs """
    job_list = Jobs.objects.order_by('-date_added').all()

    paginator = Paginator(job_list, 5)
    page = request.GET.get('page', 1)

    search_form = SearchForm()

    try:
        job_list = paginator.page(page)
    except PageNotAnInteger:
        job_list = paginator.page(1)
    except EmptyPage:
        job_list = page(paginator.num_pages)

    template = 'jobs/all_jobs.html'
    context = {
        'search_form': search_form,
        'job_list': job_list,

    }

    return render(request, template, context)


def search(request):

    if request.method == 'GET':
        search_form = SearchForm()
        search = request.GET.get('description')
        if search == '' or search == None:
            job_list = None
        else:
            job_list = Jobs.objects.order_by(
                '-date_added').filter(description__icontains=search)

            paginator = Paginator(job_list, 5)
            page = request.GET.get('page', 1)

            try:
                job_list = paginator.page(page)
            except PageNotAnInteger:
                job_list = paginator.page(1)
            except EmptyPage:
                job_list = page(paginator.num_pages)

    template = 'jobs/results.html'
    context = {
        'search_form': search_form,
        'job_list': job_list,

    }

    return render(request, template, context)


@login_required
def add_job(request):
    """ A view to add a new job """
    form = JobsForm(request.GET)

    if request.method == 'POST':
        form = JobsForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(
                request, 'You have successfully added a new job! Would you like to add another job?')
            return redirect(reverse('add_job'))
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
    recruiter = RecruiterProfile.objects.filter(user=job.author).first()
    #user1 = User.objects.filter(username=recruiter.user)

    template = 'jobs/job_profile.html'
    context = {
        'title': 'Job profile',
        'job': job,
        'recruiter': recruiter,
        # 'user1': user1,
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
