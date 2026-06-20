import requests

url = "http://127.0.0.1:5000/admin/pacientes"

token = "PEGA_AQUI_TOKEN"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

data = {
    "nombre": "Juan Pérez",
    "telefono": "600123123"
}

res = requests.post(url, json=data, headers=headers)

print(res.status_code)
print(res.json())