import uuid

from django.db import models


class SearchResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Price(models.Model):
    amount = models.IntegerField(default=0)
    currency = models.CharField(max_length=10, default="KZT")
