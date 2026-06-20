from app.extensions import db


class Doctor(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    especialidad = db.Column(
        db.String(100),
        nullable=False
    )