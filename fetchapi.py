url=input('Enter url you want to fetch from (Demo: https://fakestoreapi.com/products) _')

import requests

print("Loading... Please wait.")
r=requests.get(url)
print(r.json())