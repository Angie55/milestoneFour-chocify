from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def all_products(request):
    '''
    Accesses all products and categories in the database.
    The products are displayed 9 per page.
    '''
    products = Product.objects.all()
    categories = Category.objects.all().order_by("id")
    # Pagination code
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 3)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, "products.html", {"products": products,
                                             "categories": categories})


def product_details(request, product_id):
    '''
    Accesses all products and displays details for a
    specific product by it's id.
    '''
    products = Product.objects.all()
    if product_id:
        products = get_object_or_404(Product, id=product_id)

    return render(request, "product_details.html", {"products": products})


def products_by_category(request, category_id):
    '''
    Accesses all products and categories and displays all
    the products in a specific category by it's id.
    '''
    categories = Category.objects.all()
    products = Product.objects.all().order_by("id")
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)
    return render(request, "products_by_category.html", {"products": products,
                                                         "categories":
                                                         categories})
