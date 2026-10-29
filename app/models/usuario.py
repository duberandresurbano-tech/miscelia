from app import db
from datetime import datetime
from argon2 import PasswordHasher

ph = PasswordHasher()

class Rol(db.Model):
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False) # Ej: Administrador, Cajero
    descripcion = db.Column(db.String(200))
    
    # Relación con usuarios
    usuarios = db.relationship('Usuario', backref='rol', lazy=True)

    def __repr__(self):
        return f'<Rol {self.nombre}>'


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    activo = db.Column(db.Boolean, default=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Llave foránea para el rol
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    def set_password(self, password):
        """Hashea la contraseña usando Argon2 de forma segura"""
        self.password_hash = ph.hash(password)

    def check_password(self, password):
        """Verifica si la contraseña coincide con el hash almacenado"""
        try:
            return ph.verify(self.password_hash, password)
        except Exception:
            return False

    def __repr__(self):
        return f'<Usuario {self.username}>'