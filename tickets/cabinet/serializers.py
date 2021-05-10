from rest_framework import serializers
from auth_.models import MainUser
from airflow.serializers import OrderInfoSerializer


class CabinetUserSerializer(serializers.ModelSerializer):
    orders = OrderInfoSerializer(many=True)

    class Meta:
        model = MainUser
        fields = ['orders']
