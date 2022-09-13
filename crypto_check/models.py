import json

import requests
from django.db import models

# Create your models here.


class Crypto(models.Model):
    crypto_name = models.CharField(max_length=25)
    currency = models.CharField(max_length=3, choices=(("usd", "USD"), ("pln", "PLN"), ("eur", "EUR"), ("gbp", "GBP")),
                                default="usd")

    class Meta:
        ordering = ('crypto_name',)

