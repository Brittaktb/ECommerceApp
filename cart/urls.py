from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.view_cart, name="cart"),
    path('cart/<int:product_id>/', views.add_to_cart, name='add-to-cart'),
]