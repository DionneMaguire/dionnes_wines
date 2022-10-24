from django.contrib import admin
from .models import Wine, Category

# Register your models here.
admin.site.register(Wine)
admin.site.register(Category)