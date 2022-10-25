from django.contrib import admin
from .models import Wine, Category

# Register your models here.

class WineAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'category',
        'grape_type',
        'price',
        'image',
    )
    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    ) 

admin.site.register(Wine, WineAdmin)
admin.site.register(Category, CategoryAdmin)