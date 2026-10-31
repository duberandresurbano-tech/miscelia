from flask import Blueprint, render_template
from app.services.finanzas_manager import FinanzasManager

finanzas_bp = Blueprint('finanzas', __name__, url_prefix='/finanzas')

@finanzas_bp.route('/')
def index():
    # Obtenemos los datos reales con el servicio que ya tenemos creado
    resumen = FinanzasManager.calcular_balance_diario()
    
    return render_template(
        'finanzas/index.html',
        total_ventas=resumen.get('ventas', 0.0),
        total_gastos=resumen.get('gastos', 0.0),
        balance_neto=resumen.get('balance_neto', 0.0)
    )