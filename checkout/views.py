from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiles.models import User, RecruiterProfile
from plans.models import PlanSubscription, Plans
import stripe


def get_user(request):
    user = User.objects.filter(pk=request.user.id)
    if user.exists():
        return user.first()
    return None


def get_recruiter_profile(request):
    recruiter_profile = RecruiterProfile.objects.filter(user=request.user)
    if recruiter_profile.exists():
        return recruiter_profile.first()
    return None


@login_required
def payment(request):
    publishable_key = settings.STRIPE_PUBLISHABLE_KEY

    user = get_user(request)

    pricing_plan = Plans.objects.filter(plan_type='Recruiter plan').first()

    if request.method == "POST":
        token = request.POST['stripeToken']

        customer = stripe.Customer.retrieve(user.stripe_customer_id)
        customer.source = token
        customer.save()

        subscription = stripe.Subscription.create(
            customer=user.stripe_customer_id,
            items=[
                {"price": pricing_plan.stripe_pricing_id},
            ]
        )

        return redirect(reverse('confirmation',
                                kwargs={
                                    'subscription_id': subscription.id
                                }))

    template = 'checkout/checkout.html'
    context = {
        'publishable_key': publishable_key

    }

    return render(request, template, context)


@login_required
def confirmation(request, subscription_id):
    user = get_user(request)
    pricing_plan = Plans.objects.filter(plan_type='Recruiter plan').first()
    user.is_job_seeker = False
    user.plan_type = pricing_plan
    user.save()

    recruiter_profile = get_recruiter_profile(request)
    plan_subscription, created = PlanSubscription.objects.get_or_create(
        recruiter_profile=recruiter_profile)
    plan_subscription.stripe_subscription_id = subscription_id
    plan_subscription.active = True
    plan_subscription.save()

    messages.success(
        request, 'Thank you for your recurrent payment! You are now able to post your developer vacancies.')

    template = 'checkout/confirmation.html'
    context = {
        'subscription_id': subscription_id,
        'first_name': user.first_name,

    }

    return render(request, template, context)
