from django.contrib import admin
from .models import Product, Offer
# Register your models here.


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

admin.site.register(Product, ProductAdmin) 
admin.site.register(Offer, OfferAdmin) 