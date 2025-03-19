from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    source = models.CharField(max_length=100)
    published_at = models.DateTimeField()

class Stock(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    price = models.FloatField()
    change = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Weather(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    wind_speed = models.FloatField()
    description = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
