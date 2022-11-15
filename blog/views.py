from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Blog
from .forms import BlogForm


def blog_list(request):
    """
    Displays Blog list
    """
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, blog_id):
    """
    A view to show the blog details
    """
    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_detail.html', context)


def add_blog(request):
    """
    Add a blog to the website,
    Only superuser can do this
    """
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Successfully added Blog!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request,
                           'Failed to add blog.'
                           'Please ensure the form is valid.')
    else:
        form = BlogForm()

    context = {
        'form': form,
    }

    return render(request, 'blog/add_blog.html', context)
