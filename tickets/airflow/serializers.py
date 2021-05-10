from rest_framework import serializers
from airflow.models import *
from .utils.constants import *


class OfferListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightOrder
        fields = ('offer_id',)
        extra_kwargs = {
            'id': {'read_only': True},
            'offer_id': {'write_only': True},
            'user': {'read_only': True},
            'status': {'read_only': True},
            'price': {'read_only': True},
            'currency': {'read_only': True},
            'duration': {'read_only': True},
            'airline': {'read_only': True},
            'origin': {'read_only': True},
            'destination': {'read_only': True},
            'departure_at': {'read_only': True},
            'arrival_at': {'read_only': True}
        }

    def create(self, validated_data):
        user = self.context.get('user')
        offer_id = validated_data['offer_id']
        offer = Offer.objects.get(id=offer_id)

        order = FlightOrder.objects.create(user=user, offer_id=offer_id, status=PROCESS_PENDING, price=offer.price,
                                           currency=offer.currency,
                                           duration=offer.duration, airline=offer.airline, origin=offer.origin,
                                           destination=offer.destination, departure_at=offer.departure_at,
                                           arrival_at=offer.arrival_at)

        return order


class OrderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ('email', 'first_name', 'last_name')


class OrderInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightOrder
        exclude = ['user', 'offer_id']
