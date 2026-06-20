from app import create_app
from app.extensions import db
from app.models.user import User

app = create_app()

with app.app_context():

    admin = User(
        username="admin",
        password="admin",
        role="admin"
    )

    db.session.add(admin)
    db.session.commit()

    print("Admin creado correctamente")