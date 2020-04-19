from django.shortcuts import render, redirect, reverse


def view_cart(request):
    """
    The view that renders the cart page with products that have
    been added.
    """
    return render(request, "cart.html")


def add_to_cart(request, id):
    """
    Adds a product to the cart in specified quantity
    """
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('products'))


def adjust_cart(request, id):
    """
    Adjusts the quantity of the product in the cart
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
