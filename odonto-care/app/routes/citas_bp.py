from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.cita import Cita
from app.models.paciente import Paciente
from app.models.doctor import Doctor
from app.models.centro import Centro
from app.utils.jwt_required import token_required

citas_bp = Blueprint("citas_bp", __name__)

# Crear cita
@citas_bp.route("", methods=["POST"])
@token_required
def crear_cita(user_data):

    data = request.get_json()

    if not all([
        data.get("fecha"),
        data.get("motivo"),
        data.get("id_paciente"),
        data.get("id_doctor"),
        data.get("id_centro")
    ]):
        return jsonify({"error": "Faltan datos obligatorios"}), 400

    paciente = Paciente.query.get(data.get("id_paciente"))
    doctor = Doctor.query.get(data.get("id_doctor"))
    centro = Centro.query.get(data.get("id_centro"))

    if not paciente:
        return jsonify({"error": "Paciente no existe"}), 404

    if not doctor:
        return jsonify({"error": "Doctor no existe"}), 404

    if not centro:
        return jsonify({"error": "Centro no existe"}), 404

    if paciente.estado != "ACTIVO":
        return jsonify({"error": "Paciente inactivo"}), 400

    cita_existente = Cita.query.filter_by(
        id_doctor=data["id_doctor"],
        fecha=data["fecha"]
    ).first()

    if cita_existente:
        return jsonify({"error": "Doctor ocupado"}), 400

    cita = Cita(
        fecha=data["fecha"],
        motivo=data["motivo"],
        estado="PROGRAMADA",
        id_paciente=data["id_paciente"],
        id_doctor=data["id_doctor"],
        id_centro=data["id_centro"],
        id_usuario_registra=user_data["user_id"]
    )

    db.session.add(cita)
    db.session.commit()

    return jsonify({
        "msg": "Cita creada",
        "id": cita.id
    }), 201


# Listar citas
@citas_bp.route("", methods=["GET"])
@token_required
def listar_citas(user_data):

    query = Cita.query

    doctor = request.args.get("doctor")
    paciente = request.args.get("paciente")
    centro = request.args.get("centro")
    fecha = request.args.get("fecha")
    estado = request.args.get("estado")

    if doctor:
        query = query.filter_by(id_doctor=int(doctor))

    if paciente:
        query = query.filter_by(id_paciente=int(paciente))

    if centro:
        query = query.filter_by(id_centro=int(centro))

    if fecha:
        query = query.filter(Cita.fecha.like(f"%{fecha}%"))

    if estado:
        query = query.filter_by(estado=estado)

    citas = query.order_by(Cita.fecha.desc()).all()

    return jsonify([
        {
            "id": c.id,
            "fecha": str(c.fecha) if c.fecha else None,
            "motivo": c.motivo,
            "estado": c.estado,
            "id_paciente": c.id_paciente,
            "id_doctor": c.id_doctor,
            "id_centro": c.id_centro
        }
        for c in citas
    ])


# Cancelar cita
@citas_bp.route("/<int:cita_id>", methods=["PUT"])
@token_required
def cancelar_cita(user_data, cita_id):

    cita = Cita.query.get(cita_id)

    if not cita:
        return jsonify({"error": "Cita no encontrada"}), 404

    if cita.estado == "CANCELADA":
        return jsonify({"error": "Ya estaba cancelada"}), 400

    cita.estado = "CANCELADA"

    db.session.commit()

    return jsonify({
        "msg": "Cita cancelada"
    })