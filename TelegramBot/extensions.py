import requests
import json
from config import keys
class APIExcemption(Exception):
    pass
class Converter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIExcemption (f'Вы пытаетесь перевести одинаковые валюты.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
          raise APIExcemption (f'Такого значения нет в моём списке валют: {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
          raise APIExcemption (f'Такого значения нет в моём списке валют: {base}')
        try:
            amount = float(amount)
        except ValueError:
          raise APIExcemption (f'Не удалось обработать число :{amount}\nВ качестве третьего значения \
требуется указать только целое или нецелое число.')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        convert_value = json.loads(r.content)[keys[base]]
        convert_sum = convert_value * amount
        return convert_sum