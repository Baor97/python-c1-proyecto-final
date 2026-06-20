from flask import Blueprint, request, jsonify

from app.extensions import db

from app.models.user import User
from app.models.paciente import Paciente
from app.models.doctor import Doctor
from app.models.centro import Centro

from app.utils.jwt_required import token_required

admin_bp = Blueprint("admin_bp", __name__)


@admin_bp.route("/usuario", methods=["POST"])
@token_required
def crear_usuario(user_data):

    if user_data["role"] != "admin":
        return jsonify({"error": "No autorizado"}), 403

    data = request.get_json()

    usuario = User(
        username=data["username"],
        password=data["password"],
        role=data["role"]
    )

    db.session.add(usuario)
    db.session.commit()

    return jsonify({
        "msg": "Usuario creado"
    })


@admin_bp.route("/pacientes", methods=["POST"])
@token_required
def crear_paciente(user_data):

    if user_data["role"] != "admin":
        return jsonify({"error": "No autorizado"}), 403

    data = request.get_json()

    paciente = Paciente(
        nombre=data["nombre"],
        telefono=data.get("telefono"),
        estado=data.get("estado", "ACTIVO")
    )

    db.session.add(paciente)
    db.session.commit()

    return jsonify({
        "msg": "Paciente creado"
    })


@admin_bp.route("/pacientes", methods=["GET"])
@token_required
def listar_pacientes(user_data):

    if user_data["role"] != "admin":
        return jsonify({"error": "No autorizado"}), 403

    pacientes = Paciente.query.all()

    return jsonify([
        {
            "id": p.id,
            "nombre": p.nombre,
            "telefono": p.telefono,
            "estado": p.estado
        }
        for p in pacientes
    ])


@admin_bp.route("/doctores", methods=["POST"])
@token_required
def crear_doctor(user_data):

    if user_data["role"] != "admin":
        return jsonify({"error": "No autorizado"}), 403

    data = request.get_json()

    doctor = Doctor(
        nombre=data["nombre"],
        especialidad=data["especialidad"]
    )

    db.session.add(doctor)
    db.session.commit()

    return jsonify({
        "msg": "Doctor creado"
    })


@admin_bp.route("/centros", methods=["POST"])
@token_required
def crear_centro(user_data):

    if user_data["role"] != "admin":
        return jsonify({"error": "No autorizado"}), 403

    data = request.get_json()

    centro = Centro(
        nombre=data["nombre"],
        direccion=data["direccion"]
    )

    db.session.add(centro)
    db.session.commit()

    return jsonify({
        "msg": "Centro creado"
    })