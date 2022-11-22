from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import CustomerReviewForm
from .models import CustomerReview
from profiles.models import UserProfile

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


def about_us(request):
    """
    Function to retrieve the About Us page
    """
    return render(request, 'home/about_us.html')


def privacy_policy(request):
    """
    Function to retrieve the privacy policy page
    """
    return render(request, 'home/privacy_policy.html')


def faq(request):
    """
    Function to retrieve the faq page
    """
    return render(request, 'home/faq.html')


def add_review(request):
    """
    A view to add a customer review
    """
    if request.method == 'POST':
        form = CustomerReviewForm(request.POST)
        if form.is_valid():
            form.instance.is_customer = request.user.is_authenticated
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
