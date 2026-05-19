import requests

headers = {
    "Custom-Header": "Hello"
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    headers=headers
)

print(response.status_code)