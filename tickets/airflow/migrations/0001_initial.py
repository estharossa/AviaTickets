# Generated by Django 3.2 on 2021-04-25 11:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchResultItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('currency', models.CharField(max_length=3, verbose_name='Валюта')),
                ('duration', models.IntegerField(verbose_name='Время полета')),
                ('airline', models.CharField(max_length=10, verbose_name='Авиакомпания')),
                ('departure_at', models.DateField(verbose_name='Дата вылета')),
                ('arrival_at', models.DateField(verbose_name='Дата прилета')),
            ],
        ),
        migrations.CreateModel(
            name='SearchResult',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=3, verbose_name='Откуда')),
                ('destination', models.CharField(max_length=3, verbose_name='Куда')),
                ('departure_at', models.DateField(verbose_name='Дата вылета')),
                ('items', models.ManyToManyField(to='airflow.SearchResultItem')),
            ],
        ),
    ]
