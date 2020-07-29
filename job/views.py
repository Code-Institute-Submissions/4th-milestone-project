from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import JobForm
from .models import Job, Author
from .utils import get_author


def all_jobs(request):
    """ A view to return the job page """

    return render(request, 'job/job.html')

@login_required
def add_job(request):
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