from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Wine, Category, WineReview
from .forms import WineForm, WineReviewForm

# Create your views here.


def all_wines(request):
    """ A view to show all wines, including sorting and search queries """

    wines = Wine.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                wines = wines.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            wines = wines.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            wines = wines.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('wines'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            wines = wines.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'wines': wines,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'wines/wines.html', context)


def wine_detail(request, wine_id):
    """
    A view to show individual wine details 
    And any wine reviews for the individual wine
    """

    wine = get_object_or_404(Wine, pk=wine_id)
    reviews = wine.reviews.order_by('date_created').filter(status=1)

    context = {
        'wine': wine,
        'reviews': reviews,
    }

    return render(request, 'wines/wine_detail.html', context)


@login_required
def add_wine(request):
    """ Add a wine to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = WineForm(request.POST, request.FILES)
        if form.is_valid():
            wine = form.save()
            messages.success(request, 'Successfully added wine!')
            return redirect(reverse('wine_detail', args=[wine.id]))
        else:
            messages.error(request,
                           'Failed to add wine.'
                           'Please ensure the form is valid.')
    else:
        form = WineForm()

    template = 'wines/add_wine.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_wine(request, wine_id):
    """ Edit a wine in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    wine = get_object_or_404(Wine, pk=wine_id)
    if request.method == 'POST':
        form = WineForm(request.POST, request.FILES, instance=wine)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated wine!')
            return redirect(reverse('wine_detail', args=[wine.id]))
        else:
            messages.error(request,
                           'Failed to update wine.'
                           'Please ensure the form is valid.')
    else:
        form = WineForm(instance=wine)
        messages.info(request, f'You are editing {wine.name}')

    template = 'wines/edit_wine.html'
    context = {
        'form': form,
        'wine': wine,
    }

    return render(request, template, context)


@login_required
def delete_wine(request, wine_id):
    """ Delete a wine from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    wine = get_object_or_404(Wine, pk=wine_id)
    wine.delete()
    messages.success(request, f'{wine.name} deleted!')
    return redirect(reverse('wines'))


def add_wine_review(request, wine_id):
    """
    Add a wine review 
    """
    wine = get_object_or_404(Wine, pk=wine_id)

    if request.method == 'POST':
        form = WineReviewForm(request.POST)
        if form.is_valid():
            form.instance.is_customer = request.user.is_authenticated
            form.instance.wine = wine
            review = form.save()
            messages.success(request, 'Successfully added Wine Review!')
            return redirect(reverse('wine_detail', args=[wine.id]))
        else:
            messages.error(request,
                           'Failed to add wine review.'
                           'Please ensure the form is valid.')
    else:
        form = WineReviewForm()

    template = 'wines/add_wine_review.html'
    context = {
        'form': form,
        'wine': wine,
    }

    return render(request, template, context)