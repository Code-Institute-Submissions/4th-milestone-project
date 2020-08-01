from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, get_user
from .models import User, JobSeekerProfile, RecruiterProfile, WorkExperience
from .forms import UserForm, JobSeekerProfileForm, RecruiterProfileForm, WorkExperienceForm


@login_required
def login_success(request):
    """ Display user's profile. """

    if request.user.is_job_seeker:
        return redirect('candidate_profile')
    else:
        return redirect('recruiter_profile')


@ login_required
def candidate_profile(request):
    """ Display job seeker's profile. """

    job_seeker_profile = request.user.jobseekerprofile

    work_experience = get_object_or_404(
        WorkExperience, pk=job_seeker_profile.id)

    if request.method == 'POST':

        user_form = UserForm(request.POST,
                             request.FILES,
                             instance=request.user)

        profile_form = JobSeekerProfileForm(
            request.POST, instance=job_seeker_profile)

        work_experience_form = WorkExperienceForm(
            request.POST, instance=work_experience)

        if user_form.is_valid() and profile_form.is_valid() and work_experience_form.is_valid():
            user_form.save()
            profile_form.save()

            work_experience_form.job_title = work_experience_form.cleaned_data.get(
                'job_title')
            work_experience_form.start_date = work_experience_form.cleaned_data.get(
                'start_date')
            work_experience_form.end_date = work_experience_form.cleaned_data.get(
                'end_date')

            work_experience_form.save()

            messages.success(request, 'Profile updated successfully')
            return redirect(reverse('view_home'))
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = JobSeekerProfileForm(
            instance=request.user.jobseekerprofile)
        work_experience_form = WorkExperienceForm(
            instance=work_experience)

    first_name = request.user.first_name

    template = 'profiles/candidate_profile.html'
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'work_experience_form': work_experience_form,
        'first_name': first_name,
    }

    return render(request, template, context)


@ login_required
def recruiter_profile(request):
    """ Display recruiter's profile. """

    if request.method == 'POST':
        user_form = UserForm(request.POST,
                             request.FILES,
                             instance=request.user)
        profile_form = RecruiterProfileForm(
            request.POST, instance=request.user.recruiterprofile)
        if user_form.is_valid() and profile_form.is_valid():
            forms = user_form.save(commit=False)
            forms.save()
            forms.recruiterprofile.company_name = profile_form.cleaned_data.get(
                'company_name')
            forms.recruiterprofile.company_address1 = profile_form.cleaned_data.get(
                'company_address1')
            forms.recruiterprofile.company_address2 = profile_form.cleaned_data.get(
                'company_address2')
            forms.recruiterprofile.company_city = profile_form.cleaned_data.get(
                'company_city')
            forms.recruiterprofile.company_ZIP = profile_form.cleaned_data.get(
                'company_ZIP')
            forms.recruiterprofile.company_state = profile_form.cleaned_data.get(
                'company_state')
            forms.recruiterprofile.company_country = profile_form.cleaned_data.get(
                'company_country')

            forms.recruiterprofile.save()
            messages.success(request, 'Profile updated successfully')
            return redirect(reverse('view_home'))
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = RecruiterProfileForm(
            instance=request.user.recruiterprofile)

    first_name = request.user.first_name
    template = 'profiles/recruiter_profile.html'
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'first_name': first_name,
    }

    return render(request, template, context)
