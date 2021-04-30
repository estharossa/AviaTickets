import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models


class FareFamily:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=32)
    price = models.IntegerField(verbose_name='Цена')
    currency = models.CharField(max_length=3, verbose_name='Валюта', default='KZT')


# TODO: refactor fields using choices
class SearchResultItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')
    price = models.IntegerField(verbose_name='Цена')
    currency = models.CharField(max_length=3, verbose_name='Валюта', default='KZT')
    duration = models.IntegerField(verbose_name='Время полета')
    airline = models.CharField(max_length=32, blank=False, verbose_name='Авиакомпания')
    origin = models.CharField(max_length=3, blank=False, null=False, verbose_name='Откуда', default='ALA')
    destination = models.CharField(max_length=3, blank=False, null=False, verbose_name='Куда', default='NQZ')
    departure_at = models.DateTimeField(verbose_name='Дата вылета')
    arrival_at = models.DateTimeField(verbose_name='Дата прилета')

    def __str__(self):
        return f'{self.origin}-{self.destination}, {self.departure_at}'


class SearchResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')
    origin = models.CharField(max_length=3, blank=False, null=False, verbose_name='Откуда')
    destination = models.CharField(max_length=3, blank=False, null=False, verbose_name='Куда')
    departure_at = models.DateField(verbose_name='Дата вылета')
    items = models.ManyToManyField(SearchResultItem)

    def __str__(self):
        return f'{self.origin}-{self.destination}, {self.departure_at}'
