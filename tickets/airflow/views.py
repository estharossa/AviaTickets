from rest_framework import viewsets, generics, mixins
from rest_framework.response import Response
from airflow.utils import *

from airflow.serializers import *
from rest_framework.permissions import *


class SearchResultsView(generics.CreateAPIView):
    serializer_class = SearchResultItemSerializer
    queryset = SearchResultItem.objects.all()
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        query = request.data['query']
        search_params = SearchParams(query)

        queryset = self.get_queryset().filter(origin=search_params.origin, destination=search_params.destination,
                                              departure_at=search_params.date)
        serializer = SearchResultItemSerializer(queryset, many=True)
        return Response(serializer.data)
