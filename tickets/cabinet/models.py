from django.db import models
import uuid
from auth_.models import MainUser
from payment.utils import constants


class BankCard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')
    card_type = models.IntegerField(choices=constants.BANK_CARD_TYPE, default=0)
    card_number = models.CharField(max_length=255, unique=True, verbose_name="Номер карты")
    full_name = models.CharField(max_length=255, verbose_name="Имя Фамилия")
    expires_at = models.CharField(max_length=5, verbose_name="Годен до")
    cvv = models.IntegerField(verbose_name="CVV")
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = "Банковская карта"
        verbose_name_plural = "Банковские карты"

    def __str__(self):
        return f"{self.id} - {self.card_number} - {self.user.first_name}"
