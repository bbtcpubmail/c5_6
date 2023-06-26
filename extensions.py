import requests
import json
from config import JSON_CURRENCY_API


class Exchanger:
    @staticmethod
    def get_currencies() -> str:
        d = Exchanger.get_json()['Valute']
        cur_list = ''
        for cur in d.values():
            cur_list += cur['CharCode'] + ' - ' + cur['Name'] + '\n'
        return cur_list

    @staticmethod
    def get_json():
        r = requests.get(JSON_CURRENCY_API)
        if r.status_code == 200:
            return json.loads(r.content)

    @staticmethod
    def get_price(char_code_base: str, char_code_target: str, amount: float) -> str:
        d = Exchanger.get_json()['Valute']

        if char_code_base == 'RUB':
            base = 1
            base_nominal = 1
        else:
            base = d[char_code_base]['Value']
            base_nominal = d[char_code_base]['Nominal']
        if char_code_target == 'RUB':
            target = 1
            target_nominal = 1
        else:
            target = d[char_code_target]['Value']
            target_nominal = d[char_code_target]['Nominal']

        return round(((base / base_nominal) / (target / target_nominal)) * amount, 4)


# ex = Exchanger()
# result = ex.cur_exchange('EUR', 'RUB', 100)
# print(result)
# r = requests.get(JSON_CURRENCY_API)
# print(r.status_code)
