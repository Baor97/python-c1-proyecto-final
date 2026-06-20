import requests

BASE_URL = "http://127.0.0.1:5000"


# =========================
# 1. LOGIN
# =========================
login_data = {
    "username": "admin",
    "password": "1234"
}

login_response = requests.post(
    f"{BASE_URL}/auth/login",
    json=login_data
)

token = login_response.json()["token"]

print("TOKEN OBTENIDO")
print(token)
print("\n")


headers = {
    "Authorization": f"Bearer {token}"
}


# =========================
# 2. CREAR PACIENTE
# =========================
paciente = requests.post(
    f"{BASE_URL}/admin/pacientes",
    json={
        "nombre": "Juan Perez",
        "telefono": "600123123"
    },
    headers=headers
)

print("PACIENTE:")
print(paciente.json())
print("\n")


# =========================
# 3. CREAR DOCTOR
# =========================
doctor = requests.post(
    f"{BASE_URL}/admin/doctores",
    json={
        "nombre": "Dr. Lopez",
        "especialidad": "Ortodoncia"
    },
    headers=headers
)

print("DOCTOR:")
print(doctor.json())
print("\n")


# =========================
# 4. CREAR CENTRO
# =========================
centro = requests.post(
    f"{BASE_URL}/admin/centros",
    json={
        "nombre": "Clinica Central",
        "direccion": "Barcelona"
    },
    headers=headers
)

print("CENTRO:")
print(centro.json())
print("\n")


# =========================
# 5. CREAR CITA
# =========================
cita = requests.post(
    f"{BASE_URL}/citas",
    json={
        "fecha": "2026-06-20 10:00",
        "motivo": "Revision general",
        "id_paciente": 1,
        "id_doctor": 1,
        "id_centro": 1
    },
    headers=headers
)

print("CITA CREADA:")
print(cita.json())
print("\n")