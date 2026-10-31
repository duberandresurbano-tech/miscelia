from flask import Blueprint, render_template

pos_bp = Blueprint('pos', __name__, url_prefix='/pos')

@pos_bp.route('/')
def index():
    return "🛒 Módulo de Punto de Venta (POS) en construcción"