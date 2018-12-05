#payments------------doing!!-------getprice
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from issues.models import Issue

import stripe


# ----------link to here from profile make payment button
#        in profile use session to store details of feature --see cart
#           must add price somewhere.

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def payment(request):
    if request.method=="POST" and 'payment' not in request.POST:
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        feature=int(request.POST['feature'])
        total = 10 
        total = int(request.POST['price'])
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

                #user_id = request.user.id
                
            order_line_item = OrderLineItem(
                    order = order, 
                    feature = feature,
                    )
            order_line_item.save()
     
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if customer.paid:
                messages.error(request, "You have successfully paid")
                #--here update profilr------------------------------#########
               # current_user = request.user
                user = User.objects.get(pk=request.user.id)
                user.profile.paid_features += str(feature) + ","
                user.save()
                return redirect(reverse('get_profile'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
 
    price=request.POST['price']
    feature=request.POST['feature']
    return render(request, "payment.html", {'price':price,
                                'feature': feature,
                                'order_form': order_form, 
                                'payment_form': payment_form, 
                                'publishable': settings.STRIPE_PUBLISHABLE})        




