from django.shortcuts import render
from products.models import Category
from .forms import ContactForm


def index(request):
    """A view that displays the index page"""
    categories = Category.objects.all()
    return render(request, "index.html", {"categories": categories})


def about(request):
    """A view that displays the about us page"""
    return render(request, "about_us.html")


def contact(request):
    """
    A view that displays the contact us page.
    """

    contact_form = ContactForm()

    return render(request, "contact_us.html", {'contact_form': contact_form})
