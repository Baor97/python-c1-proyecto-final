import requests

url = "http://127.0.0.1:5000/auth/login"

data = {
    "username": "admin",
    "password": "1234"
}

res = requests.post(url, json=data)

print(res.json())