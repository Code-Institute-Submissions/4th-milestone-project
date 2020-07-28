from django.shortcuts import render, redirect, reverse
from .forms import JobForm
from .models import Job


def all_jobs(request):
    """ A view to return the job page """

    return render(request, 'job/job.html')

def add_job(request):
    form = JobForm(request.GET)
    
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('all_jobs'))
    # Empty form instantiation in order to make error messages working correctly
    else: 
        form = JobForm()

    template = 'job/add_job.html'
    context = {
        'form': form,
    }

    return render(request, template, context)