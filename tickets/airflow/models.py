import uuid

from django.db import models


class Price(models.Model):
    amount = models.IntegerField(default=0)
    currency = models.CharField(max_length=3, default="KZT")


class SearchResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class SearchResultItem(models.Model):
    price = models.OneToOneField(Price, on_delete=models.CASCADE)


class Flight(models.Model):
    duration = models.IntegerField(blank=False)


class SegmentInfo(models.Model):
    at = models.DateField()
    airport = models.CharField(max_length=3, blank=False)
    terminal = models.CharField(blank=False)


class Baggage(models.Model):
    unit = models.CharField(max_length=10, blank=False)
    value = models.IntegerField()


class Segment(models.Model):
    airline = models.CharField(max_length=10, blank=False)
    flight_number = models.CharField(blank=False)
    departure = models.ForeignKey(SegmentInfo, on_delete=models.CASCADE)
    arrival = models.ForeignKey(SegmentInfo, on_delete=models.CASCADE)

