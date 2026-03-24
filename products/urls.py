from django.urls import path
from .views import home, product_list, product_detail, register, dashboard, wishlist

urlpatterns = [
    path('', home, name='home'),
    path('shop/', product_list, name='product_list'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('wishlist/', wishlist, name='wishlist'),
]