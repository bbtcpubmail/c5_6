import requests
import json
import telebot.types
from config import JSON_CURRENCY_API


# собственный класс исключений
class ExchangeException(Exception):
    pass


# класс - обработчик команд
class Exchanger:
    # Парсинг сообщений пользователя. Проверка корректности ввода
    @staticmethod
    def parse_message(message: telebot.types.Message) -> str:
        param_list = message.text.upper().split()
        if len(param_list) != 3:
            raise ExchangeException("Должно быть 3 параметра: код базовой валюты, код целевой валюты, количество.")
        base, quote, amount = param_list
        try:
            amount = float(amount)
        except ValueError:
            raise ExchangeException("Количество валюты указано с ошибкой.")
        return f"{amount} {base} = {Exchanger.get_price(base, quote, float(amount))} {quote}"

    # Список валют
    @staticmethod
    def get_currencies() -> str:
        d = Exchanger.get_json()['Valute']
        cur_list = ''
        for cur in d.values():
            cur_list += cur['CharCode'] + ' - ' + cur['Name'] + '\n'
        return cur_list

    # Получаем JSON-структуру с курсами валют
    @staticmethod
    def get_json():
        r = requests.get(JSON_CURRENCY_API)
        if r.status_code == 200:
            return json.loads(r.content)
        else:
            raise ExchangeException("Ошибка сервера, попробуйте позднее")

    # Разбор JSON и вывод результата
    @staticmethod
    def get_price(char_code_base: str, char_code_target: str, amount: float) -> str:
        d = Exchanger.get_json()['Valute']

        if char_code_base == 'RUB':
            base = 1
            base_nominal = 1
        else:
            try:
                base = d[char_code_base]['Value']
            except KeyError:
                raise ExchangeException("Ошибка в коде базовой валюты")
            base_nominal = d[char_code_base]['Nominal']
        if char_code_target == 'RUB':
            target = 1
            target_nominal = 1
        else:
            try:
                target = d[char_code_target]['Value']
            except KeyError:
                raise ExchangeException("Ошибка в коде целевой валюты")
            target_nominal = d[char_code_target]['Nominal']
        return round(((base / base_nominal) / (target / target_nominal)) * amount, 4)


# ex = Exchanger()
# result = ex.cur_exchange('EUR', 'RUB', 100)
# print(result)
# r = requests.get(JSON_CURRENCY_API)
# print(r.status_code)
