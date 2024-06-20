from django.shortcuts import render
from django.views import View
from products.models import Products, Categories, DiscountProducts


class LandingPageView(View):
    def get(self, request):
        products = Products.objects.all()
        categories = Categories.objects.all()
        discount_products = DiscountProducts.objects.all()
        context = {
            'products': products,
            'categories': categories,
            'discount_products': discount_products
        }
        return render(request, 'main/index.html', context)
