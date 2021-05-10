from django.urls import path
from rest_framework import routers
from airflow.views import *

router = routers.SimpleRouter()

# router.register('results', SearchResultsView.as_view(), basename='search-results')

urlpatterns = [
    path('results/', SearchResultsView.as_view(), name='search-results'),
    path('create_order/', OrderView.as_view(), name='create-order')
]
