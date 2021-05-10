# Generated by Django 3.2 on 2021-05-09 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('airflow', '0007_auto_20210507_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlightOrder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_id', models.UUIDField(verbose_name='Offer ID')),
                ('status', models.SmallIntegerField(choices=[(1, 'PROCESS_OK'), (2, 'PROCESS_PENDING'), (3, 'PROCESS_ERROR')], verbose_name='Статус заказа')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('currency', models.CharField(default='KZT', max_length=3, verbose_name='Валюта')),
                ('duration', models.IntegerField(verbose_name='Время полета')),
                ('airline', models.CharField(max_length=32, verbose_name='Авиакомпания')),
                ('origin', models.CharField(default='ALA', max_length=3, verbose_name='Откуда')),
                ('destination', models.CharField(default='NQZ', max_length=3, verbose_name='Куда')),
                ('departure_at', models.DateTimeField(verbose_name='Дата вылета')),
                ('arrival_at', models.DateTimeField(verbose_name='Дата прилета')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]