from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiles.models import User
from plans.models import PlanSubscription, Plans
import stripe


def get_user(request):
    user = User.objects.filter(pk=request.user.id)
    if user.exists():
        return user.first()
    return None


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

        return redirect(reverse('view_home'))

    template = 'checkout/checkout.html'
    context = {
        'publishable_key': publishable_key

    }

    return render(request, template, context)
