from django.urls import path, include
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.home, name="home"),
    path('shop/', views.product_list, name='shop'),
]