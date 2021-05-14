from django.urls import path
from airflow.views import *

urlpatterns = [
    path('results/', OfferView.as_view(), name='search-results'),
    path('create_order/', OrderView.as_view(), name='create-order'),
    path('offer/<str:pk>', OfferDetailsView.as_view(), name='offer-details')
]
