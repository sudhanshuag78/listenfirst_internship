import requests

params = {
    "userId": 2
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)

data = response.json()

print(data[0])