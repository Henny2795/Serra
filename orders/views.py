from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import Order, OrderItem


def checkout(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = Decimal('0.00')

    if not cart:
        return redirect('cart_detail')

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id, is_active=True)
        subtotal = product.price * quantity
        total += subtotal

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total': total,
    })


def place_order(request):
    if request.method != 'POST':
        return redirect('checkout')

    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart_detail')

    customer_name = request.POST.get('customer_name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    city = request.POST.get('city')
    state = request.POST.get('state')
    pincode = request.POST.get('pincode')

    total = Decimal('0.00')
    cart_products = []

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id, is_active=True)
        quantity = int(quantity)

        if quantity > product.stock:
            return redirect('cart_detail')

        subtotal = product.price * quantity
        total += subtotal

        cart_products.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    order = Order.objects.create(
        customer_name=customer_name,
        email=email,
        phone=phone,
        address=address,
        city=city,
        state=state,
        pincode=pincode,
        total_amount=total,
        status='Pending',
    )

    for item in cart_products:
        OrderItem.objects.create(
            order=order,
            product=item['product'],
            quantity=item['quantity'],
            price=item['product'].price,
            subtotal=item['subtotal'],
        )

        product = item['product']
        product.stock -= item['quantity']
        product.save()

    request.session['cart'] = {}

    return redirect('order_success', order_id=order.id)


def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_success.html', {'order': order})