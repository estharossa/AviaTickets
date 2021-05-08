from rest_framework import serializers
from airflow.models import *


class SearchResultItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'
