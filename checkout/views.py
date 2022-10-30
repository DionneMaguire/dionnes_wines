from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('wines'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LifPjAU6MTgGD6NlRpMVCi7rL9ff27QCOS03TiWXM9vs1SXu85QcCk3QjfrSh9VOaUWxF3EFXeJeM5gLU1C9JsI00aPfg6Mck',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
