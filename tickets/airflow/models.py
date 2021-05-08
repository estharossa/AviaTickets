import uuid

from django.db import models
from auth_.models import MainUser
from .utils.constants import *


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(blank=True, default='Описание')
    price = models.IntegerField(verbose_name='Цена')
    currency = models.CharField(max_length=3, verbose_name='Валюта', default='KZT')

    class Meta:
        abstract = True


class FareFamily(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')
    name = models.CharField(max_length=32, verbose_name='Название')
    code = models.CharField(max_length=32, verbose_name='Код')
    price = models.IntegerField(verbose_name='Цена')
    currency = models.CharField(max_length=3, verbose_name='Валюта', default='KZT')


# TODO: refactor fields using choices
class Offer(models.Model):
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


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')
    user = models.ForeignKey(MainUser(), on_delete=models.CASCADE, verbose_name='Пользователь')
    status = models.SmallIntegerField(choices=ORDER_STATUSES, verbose_name="Статус заказа")
    price = models.IntegerField(verbose_name='Цена')
    currency = models.CharField(max_length=3, verbose_name='Валюта', default='KZT')
    duration = models.IntegerField(verbose_name='Время полета')
    airline = models.CharField(max_length=32, blank=False, verbose_name='Авиакомпания')
    origin = models.CharField(max_length=3, blank=False, null=False, verbose_name='Откуда', default='ALA')
    destination = models.CharField(max_length=3, blank=False, null=False, verbose_name='Куда', default='NQZ')
    departure_at = models.DateTimeField(verbose_name='Дата вылета')
    arrival_at = models.DateTimeField(verbose_name='Дата прилета')
