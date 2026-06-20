from functools import wraps
from flask import request, jsonify
import jwt
from app.config import SECRET_KEY

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"error": "Token faltante"}), 401

        try:
            token = auth_header.split(" ")[1]

            data = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=["HS256"]
            )

        except Exception:
            return jsonify({"error": "Token inválido"}), 401

        return f(data, *args, **kwargs)

    return decorated