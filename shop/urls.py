from django.urls import path, include
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.home, name="home"),
    path('products/', views.product_list, name='product_list'),
]