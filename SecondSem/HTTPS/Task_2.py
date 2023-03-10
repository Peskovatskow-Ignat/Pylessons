"""
Изучите API сервиса https://randomuser.me/
Выведите цитату "Hi, im #NAME, im from #COUNTRY, my phone number is #PHONE"
"""

import requests

r = requests.get("https://randomuser.me/api")
name = (r.json().get("results")[0].get("name").get("first"))
country = (r.json().get("results")[0].get("location").get("country"))
phone = (r.json().get("results")[0].get("registered"))
print(f"Hi, im {name}, im from {country}, my phone number is, {phone}")
