from django.urls import path
from . import views
from .views import PaymentListView

app_name = "payments"

urlpatterns = [
    path("", PaymentListView.as_view(), name="payments"),
    path("customer_payments/", views.customer_payments_view, name="customer-payments"),
    path('process_payments/<int:order_id>/', views.process_payment, name='process_payment'),
    path('complete/<int:pk>/', views.payment_complete, name='payment_complete'),
]
