from django.contrib import admin
from .models import Brand, Category, Products
# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at','description')
    list_filter = ('is_active',)
    search_fields = ('name','description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description')
    list_filter = ('is_active',)
    search_fields = ('name','description')


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'category', 'is_active', 'price', 'description')
    list_filter = ('is_active','brand','category')
    search_fields = ('title','description')
