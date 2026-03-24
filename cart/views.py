from django.shortcuts import redirect, render, get_object_or_404
from products.models import Product


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_active=True)

    cart = request.session.get('cart', {})

    product_id_str = str(product_id)

    if product_id_str in cart:
        if cart[product_id_str] < product.stock:
            cart[product_id_str] += 1
    else:
        if product.stock > 0:
            cart[product_id_str] = 1

    request.session['cart'] = cart
    return redirect('cart_detail')


def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id, is_active=True)
        subtotal = product.price * quantity
        total += subtotal

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    return render(request, 'cart_detail.html', {
        'cart_items': cart_items,
        'total': total,
    })


def update_cart_item(request, product_id):
    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, id=product_id, is_active=True)
    product_id_str = str(product_id)

    action = request.GET.get('action')

    if product_id_str in cart:
        if action == 'increase':
            if cart[product_id_str] < product.stock:
                cart[product_id_str] += 1
        elif action == 'decrease':
            cart[product_id_str] -= 1
            if cart[product_id_str] <= 0:
                del cart[product_id_str]

    request.session['cart'] = cart
    return redirect('cart_detail')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)

    if product_id_str in cart:
        del cart[product_id_str]

    request.session['cart'] = cart
    return redirect('cart_detail')