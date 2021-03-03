import requests
import json
import time

print("Введите код валюты")
cur = input()
while True:
    d = json.loads(requests.get("https://blockchain.info/ru/ticker").text)
    print(d[cur]["last"])
    time.sleep(5)
