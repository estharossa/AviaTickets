from rest_framework import viewsets
from airflow.serializers import *
from rest_framework.permissions import *


class SearchResultViewSet(viewsets.ModelViewSet):
    serializer_class = SearchResultSerializer
    queryset = SearchResult.objects.all()
    permission_classes = (IsAuthenticated, )
