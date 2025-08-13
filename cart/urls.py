from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.view_cart, name="cart"),
    path('add/', views.add_to_cart, name='cart_add'),
    path('delete/', views.delete_from_cart, name='cart_delete'),
    path('update/', views.update_cart, name='cart_update'),
]