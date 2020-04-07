from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def all_products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, "products.html", {"products": products,
                                             "categories": categories})


def products_by_category(request, category_id):
    categories = Category.objects.all()
    products = Product.objects.all().order_by("id")
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)
    return render(request, "products_by_category.html", {"products": products,
                                                         "categories": categories,
                                                        })
