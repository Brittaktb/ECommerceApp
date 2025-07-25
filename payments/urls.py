from django.urls import path
from . import views
from .views import PaymentListView
app_name = "payments"

urlpatterns = [
    path("", PaymentListView.as_view(), name="payments-overview"),
]