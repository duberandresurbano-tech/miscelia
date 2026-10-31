from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.usuario import Usuario
from app import db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = Usuario.query.filter_by(usuario_acceso=username).first()
        
        if user and user.hash_contrasena == password:
            # ¡IMPORTANTE! Guardamos el usuario en la sesión para que el Dashboard lo deje pasar
            session['usuario_acceso'] = user.usuario_acceso
            session['nombre_usuario'] = user.nombre
            
            flash('¡Bienvenido a Miscelia!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
            
    return render_template('auth/login.html')

# --- NUEVA RUTA DE CERRAR SESIÓN ---
@auth_bp.route('/logout')
def logout():
    session.clear() # Borramos todos los datos de la sesión
    flash('Has cerrado sesión correctamente.', 'info')
    return redirect(url_for('auth.login'))