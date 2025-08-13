from django.urls import path, include
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.home, name="home"),
    path('product-list/', views.product_list, name='product-list'),
    path('product-list/<int:category_pk>/', views.product_list, name='products_by_category'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('category_summary/', views.category_summary, name='category_summary'),
]