from rest_framework import serializers
from auth_.models import MainUser
from airflow.serializers import OrderInfoSerializer
from .models import BankCard


class CabinetUserSerializer(serializers.ModelSerializer):
    orders = OrderInfoSerializer(many=True)

    class Meta:
        model = MainUser
        fields = ['orders']


class BankCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankCard
        fields = ['id', 'card_type', 'card_number', 'full_name', 'expires_at', 'cvv']
        extra_kwargs = {
            'card_type': {'write_only': True},
            'expires_at': {'write_only': True},
            'cvv': {'write_only': True}
        }

    def create(self, validated_data):
        card_type = validated_data['card_type']
        card_number = validated_data['card_number']
        full_name = validated_data['full_name']
        expires_at = validated_data['expires_at']
        cvv = validated_data['cvv']
        user = self.context.get('user')

        card = BankCard.objects.create(card_type=card_type, card_number=card_number, full_name=full_name,
                                       expires_at=expires_at, cvv=cvv, user=user)

        return card
