from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # Ruta de prueba temporal para verificar que enciende
    @app.route('/')
    def index():
        return "¡Miscelia Backend funcionando al 100%! 🚀"

    from app.models.usuario import Rol, Usuario

    return app