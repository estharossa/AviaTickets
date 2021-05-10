from django.urls import path
from .views import cabinet_orders

urlpatterns = [
    path('orders', cabinet_orders)
]
