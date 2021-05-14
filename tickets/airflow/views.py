from rest_framework import generics, status
from rest_framework.response import Response
from airflow.utils.functions import *
from airflow.serializers import *
from rest_framework.permissions import *


class OfferView(generics.CreateAPIView):
    serializer_class = OfferListSerializer
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

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class OfferDetailsView(generics.RetrieveAPIView):
    serializer_class = OfferListSerializer
    queryset = Offer.objects.all()
    permission_classes = [IsAuthenticated]


class OrderView(generics.CreateAPIView):
    serializer_class = CreateOrderSerializer
    queryset = FlightOrder.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        context = {
            'user': user
        }
        serializer = CreateOrderSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        return Response(OrderInfoSerializer(order).data)



