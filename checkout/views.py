from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe

stripe.api_key = settings.STRIPE_SECRET

'''
Checkout view gives the user the order and payment form
to fill out if they are logged in
'''
@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        # saves the order if both forms valid
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date_ordered = timezone.now()
            order.save()
            # saves what is in cart to the order
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()
            # try using Stripe API to create customer charge
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            # display error message if charge unsuccessful
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            # let's customer know if they have successfully paid
            if customer.paid:
                messages.error(request, "Thank you, your payment was successful and your order will be processed shortly.")
                request.session['cart'] = {}
                return redirect(reverse('index'))
            # gives them an error message if payment unsuccessful
            else:
                messages.error(request, "Unable to take payment")
        # prints errors where payment form filled in incorrectly
        # or unable to tp payment with that card
        else:
            print(payment_form.errors)
            messages.error(request,
                           "We were unable to take a payment with that card!")
    # returns blank payment and order form
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    # returns checkout page with forms and Stripe publishable key
    return render(request, "checkout.html", {"order_form":
                                             order_form,
                                             "payment_form":
                                             payment_form,
                                             "publishable":
                                             settings.STRIPE_PUBLISHABLE})
