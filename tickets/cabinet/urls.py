from django.urls import path
from .views import cabinet_orders
from rest_framework.routers import SimpleRouter
from .views import BankCardViewSet

router = SimpleRouter()
router.register('cards', BankCardViewSet)

urlpatterns = [
    path('orders', cabinet_orders)
] + router.urls
