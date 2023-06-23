import requests
import json
from config import JSON_CURRENCY_API

class Exchanger:
    def __init__(self):

        d = Exchanger.get_json()['Valute']
        cur_list = ''
        for cur in d.values():
            cur_list += cur['CharCode'] + ' - ' + cur['Name'] + '\n'
        self.cur_list = cur_list

    @property
    def currencies(self) -> str:
        return self.cur_list

    @staticmethod
    def get_json():
        r = requests.get(JSON_CURRENCY_API)
        return json.loads(r.content)

    @staticmethod
    def cur_exchange(char_code_base: str, char_code_target: str, amount: float) -> str:
        d = Exchanger.get_json()['Valute']

        if char_code_base == 'RUB':
            base = 1
        else:
            base = d[char_code_base]['Value']
        if char_code_target == 'RUB':
            target = 1
        else:
            target = d[char_code_target]['Value']

        return (base / target) * amount


# ex = Exchanger()
# result = ex.cur_exchange('EUR', 'RUB', 100)
# print(result)
