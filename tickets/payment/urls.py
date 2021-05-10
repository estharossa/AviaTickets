from django.urls import path
from .views import process_order

urlpatterns = [
    path('process/<uuid:order_id>', process_order)
]
