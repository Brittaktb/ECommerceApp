from django.urls import path
from .views import OrderListView
from . import views
from django.shortcuts import render, get_object_or_404


app_name = "orders"

urlpatterns = [
    path('', OrderListView.as_view(), name='all_orders'),
    path('customer_orders/', views.customer_orders_view, name="my-orders"),
    path('checkout/', views.checkout, name='checkout'),
     path('success/', lambda request: render(request, 'orders/success.html'), name='order_success'),
]

