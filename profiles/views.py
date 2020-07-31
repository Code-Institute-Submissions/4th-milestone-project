from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, get_user
from .models import User, JobSeekerProfile, RecruiterProfile
from .forms import UserForm, JobSeekerProfileForm, RecruiterProfileForm


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(User, pk=request.user.id)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=profile)
        profile_form = JobSeekerProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            forms = user_form.save(commit=False)
            forms.jobseekerprofile.save()
            messages.success(request, 'Profile updated successfully')
            return redirect(reverse('view_home'))
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        user_form = UserForm(instance=profile)
        profile_form = JobSeekerProfileForm(instance=profile)

    template = 'profiles/user_profile.html'
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, template, context)
