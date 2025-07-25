from django.contrib import admin
from .models import Product, Category, ProductImage
# Register your models here.

admin.site.register(ProductImage)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ list display shows selected product details 
        prepopulated_fields create the slugfield automatically: here the name with '-' inbetween the words"""
    list_display = ['name', 'price', 'available']
    prepopulated_fields = {'slug': ('name',)}