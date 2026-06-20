from flask import Flask
from app.extensions import db

from app.routes.auth_bp import auth_bp
from app.routes.admin_bp import admin_bp
from app.routes.citas_bp import citas_bp

from app.models.user import User
from app.models.paciente import Paciente
from app.models.doctor import Doctor
from app.models.centro import Centro
from app.models.cita import Cita


def create_app():

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///odonto.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(citas_bp, url_prefix="/citas")

    with app.app_context():
        db.create_all()

    @app.route("/")
    def home():
        return {"msg": "API OdontoCare funcionando"}

    return app