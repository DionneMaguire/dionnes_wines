from django.shortcuts import render, get_object_or_404

from .models import Blog


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
