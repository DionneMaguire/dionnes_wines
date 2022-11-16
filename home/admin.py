from django.contrib import admin
from .models import CustomerReview


class CustomerReviewAdmin(admin.ModelAdmin):
    """
    add fields for display in customer review in admin
    """
    list_display = (
        'name',
        'rating',
        'comment',
        'status',
    )


admin.site.register(CustomerReview, CustomerReviewAdmin)