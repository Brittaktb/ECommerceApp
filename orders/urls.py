from django.urls import path
from .views import OrderListView
from . import views


app_name = "orders"

urlpatterns = [
    path('', OrderListView.as_view(), name='all_orders'),
    path('customer_orders/', views.customer_orders_view, name="my-orders"),
]

