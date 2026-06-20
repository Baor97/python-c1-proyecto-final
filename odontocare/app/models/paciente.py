from app.extensions import db


class Paciente(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    telefono = db.Column(
        db.String(20)
    )

    estado = db.Column(
        db.String(20),
        default="ACTIVO"
    )