import requests

BASE = "http://127.0.0.1:5000"

response = requests.get(BASE + "/hello/anand/30")
print(response.json())

# response = requests.post(BASE + "/hello")
# print(response.json())
#
# response = requests.get(BASE + "/")
# print(response.json())
