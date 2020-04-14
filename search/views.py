from django.shortcuts import render
from products.models import Product


def do_search(request):
    '''
    Displays products that contain the word submitted
    in the search form if it is in the title.
    '''
    products = Product.objects.filter(title__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})
