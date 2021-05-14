from django.db import models
import uuid
from auth_.models import MainUser
from payment.utils import constants
from .utils import constants as cabinet_constants


class BankCard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')
    card_type = models.IntegerField(choices=constants.BANK_CARD_TYPE, default=0, verbose_name='Тип карты')
    card_number = models.CharField(max_length=255, unique=True, verbose_name='Номер карты')
    full_name = models.CharField(max_length=255, verbose_name='Имя Фамилия')
    expires_at = models.CharField(max_length=5, verbose_name='Годен до')
    cvv = models.IntegerField(verbose_name='CVV')
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return f"{self.card_number} - {self.user.first_name}"


class Passenger(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    gender = models.CharField(max_length=1, choices=cabinet_constants.GENDER_CHOICES, verbose_name='Пол')
    date_of_birth = models.DateField(verbose_name='Дата рожения')
    citizenship = models.CharField(max_length=255, verbose_name='Гражданство')
    document_number = models.CharField(max_length=255, verbose_name='Номер документа')
    expires_at = models.DateField(null=True, verbose_name='Дата истечения документа')
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'
