from django.shortcuts import render
from products.models import Category


def index(request):
    """A view that displays the index page"""
    categories = Category.objects.all()
    return render(request, "index.html", {"categories": categories})


def about(request):
    """A view that displays the about us page"""
    return render(request, "about_us.html")


def contact(request):
    """A view that displays the contact page"""
    return render(request, "contact_us.html")
