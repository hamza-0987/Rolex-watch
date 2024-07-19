from django.contrib import admin
from .models import Product

@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'image']
    search_fields = ['title']
