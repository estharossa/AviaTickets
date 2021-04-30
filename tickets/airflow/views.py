from rest_framework import generics
from rest_framework.response import Response
from airflow.utils.functions import *

from airflow.serializers import *
from rest_framework.permissions import *


class SearchResultsView(generics.CreateAPIView):
    serializer_class = SearchResultItemSerializer
    queryset = SearchResultItem.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        query = request.data['query']
        search_params = SearchParams(query)
        queryset = self.get_queryset().filter(origin=search_params.origin,
                                              destination=search_params.destination,
                                              departure_at__date=search_params.get_date())

        serializer = SearchResultItemSerializer(queryset, many=False)
        return Response(serializer.data)
