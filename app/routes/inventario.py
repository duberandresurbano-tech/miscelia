from flask import Blueprint, render_template

inventario_bp = Blueprint('inventario', __name__, url_prefix='/inventario')

@inventario_bp.route('/')
def index():
    return "📦 Módulo de Inventario funcionando"