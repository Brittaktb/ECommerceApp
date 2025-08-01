from django.urls import path, include
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.home, name="home"),
    path('product-list/', views.product_list, name='product-list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]