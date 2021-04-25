from rest_framework import serializers
from airflow.models import *


class SearchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchResult
        fields = '__all__'
