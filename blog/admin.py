from django.contrib import admin
from .models import Blog

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    """
    add fields for display in admin
    prepopulate the slug field
    """
    prepopulated_fields = {'slug': ('title',)}
    list_display = (
        'pk',
        'title',
        'slug',
        'image',
        'date_created',
    )


admin.site.register(Blog, BlogAdmin)