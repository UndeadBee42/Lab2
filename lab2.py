import requests
import json
import time

print("Введите код валюты")
cur = input()
while True:
    d = json.loads(requests.get("https://blockchain.info/ru/ticker").text)
    v = d[cur]
    print(v["last"])
    time.sleep(5)
