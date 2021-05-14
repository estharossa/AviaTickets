from django.urls import path
from .views import cabinet_orders
from rest_framework.routers import SimpleRouter
from .views import BankCardViewSet, CabinetOrderDetailsView, CabinetOrdersView, PassengerViewSet

router = SimpleRouter()
router.register('cards', BankCardViewSet)
router.register('passengers', PassengerViewSet)

urlpatterns = [
    path('orders', cabinet_orders),
    path('order_list', CabinetOrdersView.as_view(), name='orders'),
    path('order_list/<str:pk>', CabinetOrderDetailsView.as_view(), name='details')
] + router.urls
