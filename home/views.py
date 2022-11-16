from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import CustomerReviewForm
from .models import CustomerReview

# Create your views here.


def index(request):
    """ 
    A view to return the index page 
    display last 3 published reviews
    """
    reviews = CustomerReview.objects.filter(status=1)[:4]

    context = {
        'reviews': reviews
    }

    return render(request, 'home/index.html', context)


def add_review(request):
    """
    A view to add a customer review
    """
    if request.method == 'POST':
        form = CustomerReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            messages.success(request, 'Successfully added Review!')
            return redirect(reverse('home'))
        else:
            messages.error(request,
                           'Failed to add review.'
                           'Please ensure the form is valid.')
    else:
        form = CustomerReviewForm()

    context = {
        'form': form,
    }

    return render(request, 'home/add_review.html', context)
