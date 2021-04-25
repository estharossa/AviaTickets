from rest_framework import routers
from airflow.views import *

router = routers.SimpleRouter()

router.register('results', SearchResultViewSet, basename='search')

urlpatterns = router.urls
