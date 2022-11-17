from django.contrib import admin
from .models import Wine, Category, WineReview

# Register your models here.


class WineAdmin(admin.ModelAdmin):
    """
    Add fields for display and ordering in admin page
    """
    list_display = (
        'pk',
        'name',
        'category',
        'grape',
        'price',
        'image',
    )
    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Add fields for display in admin page
    """
    list_display = (
        'friendly_name',
        'name',
    )


class WineReviewAdmin(admin.ModelAdmin):
    """
    Add fields for display and ordering in admin page
    """
    list_display = (
        'wine',
        'name',
        'rating',
        'is_customer',
        'status',
    )
    ordering = ('date_created',)


admin.site.register(Wine, WineAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(WineReview, WineReviewAdmin)
