from rest_framework import serializers
from airflow.models import *


class SearchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchResult
        fields = '__all__'


class SearchResultItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchResultItem
        fields = '__all__'
