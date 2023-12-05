from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OJyeGC3dSou0Fp0AHYMauPta0Nzvgn7rWngUIzyqb2ESlR0uX7AQpncmWTjj0toS0AE5bz71QzpDzZfRWnZ0l5P00MP1bHATC',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
