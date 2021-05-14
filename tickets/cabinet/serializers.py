from rest_framework import serializers
from auth_.models import MainUser
from airflow.serializers import OrderInfoSerializer
from .models import BankCard, Passenger


class CabinetUserSerializer(serializers.ModelSerializer):
    orders = OrderInfoSerializer(many=True)

    class Meta:
        model = MainUser
        fields = ['id', 'orders']


class BankCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankCard
        fields = ['id', 'card_type', 'card_number', 'full_name', 'expires_at', 'cvv']
        extra_kwargs = {
            'card_type': {'write_only': True},
            'expires_at': {'write_only': True},
            'cvv': {'write_only': True}
        }

    def validate_card_number(self, value):
        if len(value) != 19:
            raise serializers.ValidationError('Card number length validation error')
        if not value.isdecimal():
            raise serializers.ValidationError('Card number format validation error')
        return value

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


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        exclude = ('user',)
        extra_kwargs = {
            'gender': {'write_only': True},
            'date_of_birth': {'write_only': True},
            'citizenship': {'write_only': True},
            'document_number': {'write_only': True},
            'expires_at': {'write_only': True}
        }

    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        gender = validated_data['gender']
        date_of_birth = validated_data['date_of_birth']
        citizenship = validated_data['citizenship']
        document_number = validated_data['document_number']
        expires_at = validated_data['expires_at']
        user = self.context.get('user')

        passenger = Passenger.objects.create(first_name=first_name, last_name=last_name, gender=gender,
                                             date_of_birth=date_of_birth, citizenship=citizenship,
                                             document_number=document_number, expires_at=expires_at, user=user)
        return passenger
