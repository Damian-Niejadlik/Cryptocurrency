import json
import time
from decimal import Decimal

import requests


class Crypto:
    def __init__(self, coin: str, currency: str = 'usd'):
        """
        :param coin: name of cryptocurrency (for example "bitcoin")
        :param currency: name of your currency (for example "usd")
        """
        self.coin = coin
        self.currency = currency
        self.url = f'https://api.coingecko.com/api/v3/coins/{coin}'
        self.response = requests.get(self.url)
        self.data = json.loads(self.response.content.decode('utf-8'))
        self.saved_crypto_price = self.data.get('market_data').get('current_price').get(currency)
        self.crypto_price = self.data.get('market_data').get('current_price').get(currency)

    def __str__(self):
        return f"{self.coin}: {self.crypto_price} {self.currency.upper()}"

    # def checking_loop(self):
    #     print(self)
    #     seconds = 0
    #     print("=" * 20)
    #     while True:
    #         mins, secs = divmod(seconds, 60)
    #         hours, mins = divmod(mins, 60)
    #         day, hours = divmod(hours, 24)
    #         timer = '{:02d}[day]:{:02d}[h]:{:02d}[m]:{:02d}[s]'.format(day, hours, mins, secs)
    #         time.sleep(1)
    #         seconds += 1
    #         if str(timer)[-4] == '0':
    #             self.response = requests.get(self.url)
    #             self.data = json.loads(self.response.content.decode('utf-8'))
    #             self.crypto_price = self.data.get('market_data').get('current_price').get(self.currency)
    #             if self.crypto_price > (self.saved_crypto_price * 1.02):
    #                 print(
    #                     f'In: {timer} your crypto gain {((self.crypto_price * 100 / self.saved_crypto_price) - 100):.2f}%,'
    #                     f' and now is {self.crypto_price}')
    #                 self.saved_crypto_price = self.crypto_price
    #             if self.crypto_price < (self.saved_crypto_price * 0.98):
    #                 print(
    #                     f'In: {timer} your crypto lose {((self.crypto_price * 100 / self.saved_crypto_price) - 100):.2f}%,'
    #                     f' and now is {self.crypto_price}')
    #                 self.saved_crypto_price = self.crypto_price
    def check(self):
        self.response = requests.get(self.url)
        self.data = json.loads(self.response.content.decode('utf-8'))
        self.crypto_price = Decimal(self.data.get('market_data').get('current_price').get(self.currency))
        price = f"{self.crypto_price:.2f}"
        coin = self.coin[0].upper() + self.coin[1::]

        return coin, price, self.currency.upper()
