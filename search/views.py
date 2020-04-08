from django.shortcuts import render
from products.models import Product


def do_search(request):
    products = Product.objects.filter(title__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})