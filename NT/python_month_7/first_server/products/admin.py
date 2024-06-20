from django.contrib import admin
from .models import Service, Countries, Categories, DiscountProducts, Products

admin.site.register(Service)
admin.site.register(Countries)
admin.site.register(Categories)
admin.site.register(DiscountProducts)
admin.site.register(Products)
