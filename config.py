import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'clave-secreta-super-segura-miscelia')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Conexión a PostgreSQL local (actualiza usuario y contraseña si es necesario)
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL', 
        'postgresql://postgres:tu_contraseña@localhost:5432/miscelia_db'
    )