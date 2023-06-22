import requests
import json
from config import JSON_CURRENCY_API



r = requests.get(JSON_CURRENCY_API)

d = json.loads(r.content)  # делаем из полученных байтов Python-объект для удобной работы

print(type(d))
print(list(d))
