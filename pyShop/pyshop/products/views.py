from django.shortcuts import render
from .models import Product

# Create your views here.

def main(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    
    return render(request, 'main.html', context)
