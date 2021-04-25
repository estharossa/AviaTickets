from django.contrib import admin
from airflow.models import SearchResult, SearchResultItem

admin.site.register(SearchResult)
admin.site.register(SearchResultItem)
