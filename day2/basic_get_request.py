import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

print(response)