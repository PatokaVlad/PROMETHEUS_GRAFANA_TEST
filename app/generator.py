import requests
import random

def test_conversion(value):
    url = "http://127.0.0.1:5000/event"
    data = {"value": value}  # Рядок, який потрібно перетворити на ціле число
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        print("POST request successful")
    else:
        print("POST request failed")

while(True):
    value = random.randint(10, 200)
    test_conversion(value)
