from django.urls import path
from .views import add_to_cart, cart_detail, update_cart_item, remove_from_cart

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update/<int:product_id>/', update_cart_item, name='update_cart_item'),
    path('remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
]