from flask import Blueprint, request, jsonify
import jwt
import datetime

from app.models.user import User
from app.config import SECRET_KEY

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():

    # Obtener datos del JSON enviado por el cliente
    data = request.get_json()

    if not data:
        return jsonify({"error": "Falta JSON en la petición"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Faltan credenciales"}), 400

    # Buscar usuario en la base de datos
    user = User.query.filter_by(username=username).first()

    # Validar credenciales
    if not user or user.password != password:
        return jsonify({"error": "Credenciales inválidas"}), 401

    # Crear token JWT
    token = jwt.encode(
        {
            "user_id": user.id,
            "role": user.role,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        },
        SECRET_KEY,
        algorithm="HS256"
    )

    return jsonify({
        "token": token
    })