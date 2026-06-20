from app.extensions import db

class Cita(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    fecha = db.Column(db.String(50), nullable=False)
    motivo = db.Column(db.String(200), nullable=False)

    estado = db.Column(db.String(20), default="PROGRAMADA")

    id_paciente = db.Column(
        db.Integer,
        db.ForeignKey("paciente.id"),
        nullable=False
    )

    id_doctor = db.Column(
        db.Integer,
        db.ForeignKey("doctor.id"),
        nullable=False
    )

    id_centro = db.Column(
        db.Integer,
        db.ForeignKey("centro.id"),
        nullable=False
    )

    id_usuario_registra = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )