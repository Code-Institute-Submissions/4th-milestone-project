from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, get_user
from .models import User, JobSeekerProfile, RecruiterProfile, WorkExperience, Education
from .forms import UserForm, JobSeekerProfileForm, RecruiterProfileForm, WorkExperienceForm, EducationForm


@login_required
def login_success(request):
    """ Display user's profile. """

    if request.user.is_job_seeker:
        return redirect(reverse('candidate_profile'))
    else:
        return redirect(reverse('recruiter_profile'))


@ login_required
def candidate_profile(request):
    """ Display candidate's profile. """

    user = get_object_or_404(User, id=request.user.id)

    template = 'profiles/candidate_profile.html'
    context = {
        'user': user,
    }

    return render(request, template, context)


@ login_required
def edit_candidate_profile(request):
    """ Edit candidate's profile. """
    job_seeker_profile = get_object_or_404(JobSeekerProfile, user=request.user)

    if request.method == 'POST':

        user_form = UserForm(request.POST,
                             request.FILES,
                             instance=request.user)

        profile_form = JobSeekerProfileForm(
            request.POST, instance=job_seeker_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, 'Profile updated successfully')
            return redirect(reverse('view_home'))
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = JobSeekerProfileForm(
            instance=job_seeker_profile)

    template = 'profiles/edit_candidate_profile.html'
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, template, context)


@ login_required
def edit_work_experience(request):
    """ Edit work experience candidate. """

    job_seeker = JobSeekerProfile.objects.filter(pk=request.user.id).first()

    if request.method == 'POST':

        form = WorkExperienceForm(
            request.POST)

        if form.is_valid():
            form.instance.experience_item = job_seeker
            form.save()

            messages.success(request, 'Work experience updated successfully')
            return redirect(reverse('edit_work_experience'))
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = WorkExperienceForm()

    experience_list = WorkExperience.objects.filter(experience_item=job_seeker)

    template = 'profiles/edit_work_experience.html'
    context = {
        'form': form,
        'experience_list': experience_list,

    }

    return render(request, template, context)


@ login_required
def delete_work_experience(request, experience_id):
    """ Delete work experience candidate. """
    experience_item = get_object_or_404(WorkExperience, pk=experience_id)
    job_seeker = JobSeekerProfile.objects.filter(pk=request.user.id).first()

    if request.user != job_seeker.user:
        messages.error(
            request, 'You are not allowed to remove this work experience.')
        return redirect(reverse('view_home'))

    else:
        experience_item.delete()
        messages.success(
            request, 'Your work experience is succesfully deleted.')
        return redirect(reverse('edit_work_experience'))


@ login_required
def edit_education(request):
    """ Edit education candidate. """
    job_seeker = JobSeekerProfile.objects.filter(pk=request.user.id).first()

    if request.method == 'POST':

        form = EducationForm(
            request.POST)

        if form.is_valid():
            form.instance.education_item = job_seeker
            form.save()

            messages.success(request, 'Work experience updated successfully')
            return redirect(reverse('edit_education'))
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = EducationForm()

    education_list = Education.objects.filter(education_item=job_seeker)

    template = 'profiles/edit_education.html'
    context = {
        'form': form,
        'education_list': education_list,

    }

    return render(request, template, context)


@ login_required
def delete_education(request, education_id):
    """ Delete education candidate. """
    education_item = get_object_or_404(Education, pk=education_id)
    job_seeker = JobSeekerProfile.objects.filter(pk=request.user.id).first()

    if request.user != job_seeker.user:
        messages.error(
            request, 'You are not allowed to remove this eduction.')
        return redirect(reverse('view_home'))

    else:
        education_item.delete()
        messages.success(
            request, 'Your education is succesfully deleted.')
        return redirect(reverse('edit_education'))


@ login_required
def recruiter_profile(request):
    """ Display recruiter's profile. """

    user = get_object_or_404(User, id=request.user.id)

    template = 'profiles/recruiter_profile.html'
    context = {
        'user': user,
    }

    return render(request, template, context)


@ login_required
def edit_recruiter_profile(request):
    """ Edit recruiter's profile. """
    recruiter_profile = get_object_or_404(RecruiterProfile, user=request.user)

    if request.method == 'POST':

        user_form = UserForm(request.POST,
                             request.FILES,
                             instance=request.user)

        profile_form = RecruiterProfileForm(
            request.POST, instance=recruiter_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, 'Profile updated successfully')
            return redirect(reverse('view_home'))
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = RecruiterProfileForm(
            instance=recruiter_profile)

    template = 'profiles/edit_recruiter_profile.html'
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, template, context)
