from django.shortcuts import render

from .models import CustomerReview

# Create your views here.


def index(request):
    """ A view to return the index page 
        display last 3 published reviews
    """
    reviews = CustomerReview.objects.filter(status=1)

    context = {
        'reviews': reviews
    }

    return render(request, 'home/index.html', context)
