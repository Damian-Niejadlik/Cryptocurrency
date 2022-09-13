import json

from django import forms
from .models import Crypto


class CryptoForm(forms.ModelForm):
    crypto_name = forms.CharField(error_messages={"Error": "This coin doesn't exist"}, label="Coin",
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    currency = forms.ChoiceField(choices=(("usd", "USD"), ("pln", "PLN"), ("eur", "EUR"), ("gbp", "GBP")),
                                 widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Crypto
        fields = ["crypto_name", "currency"]
