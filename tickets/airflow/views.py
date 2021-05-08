from rest_framework import generics, status
from rest_framework.response import Response
from airflow.utils.functions import *

from airflow.serializers import *
from rest_framework.permissions import *


class SearchResultsView(generics.CreateAPIView):
    serializer_class = SearchResultItemSerializer
    queryset = Offer.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        query = request.data['query']
        search_params = SearchParams(query)

        if not search_params.validate():
            content = {'Bad Request': 'Invalid query params'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        queryset = self.get_queryset().filter(origin=search_params.origin,
                                              destination=search_params.destination,
                                              departure_at__date=search_params.get_date())

        serializer = SearchResultItemSerializer(queryset, many=True)
        return Response(serializer.data)
