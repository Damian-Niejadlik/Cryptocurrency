import json

import requests
from django.shortcuts import render, redirect
from crypto_check.forms import CryptoForm


def start_view(request):
    template = 'crypto_check/home.html'
    if request.method == 'POST':
        form = CryptoForm(request.POST)
        if form.is_valid():
            coin = request.POST.get("crypto_name")
            currency = request.POST.get("currency")
            return redirect(f'{coin}/{currency}')

    else:
        form = CryptoForm()

    return render(request, template, {'form': form})


def check_view(request, name: str, currency: str):
    try:
        url = f'https://api.coingecko.com/api/v3/coins/{name}'
        response = requests.get(url)
        data = json.loads(response.content.decode('utf-8'))
        crypto_price = data.get('market_data').get('current_price').get(currency)
        coin = name[0].upper() + name[1:]

        return render(request, template_name='crypto_check/check.html', context={'crypto': coin,
                                                                                 'price': crypto_price,
                                                                                 'currency': currency.upper(),
                                                                                 })
    except AttributeError:
        return render(request, template_name='crypto_check/error.html')
