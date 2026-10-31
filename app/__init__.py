from flask import Flask, render_template, redirect, url_for
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 1. Inicializamos las extensiones con la app
    db.init_app(app)
    migrate.init_app(app, db)

    # 2. Importación de modelos
    from app.models.usuario import Rol, Usuario, usuario_rol
    from app.models.producto import Categoria, Producto, PresentacionProducto
    from app.models.proveedor import Proveedor, Compra, DetalleCompra
    from app.models.venta import Venta, DetalleVenta, HistorialCorreccionVenta
    from app.models.inventario import MovimientoInventario
    from app.models.pedido_qr import PedidoQR, DetallePedidoQR, Gasto

    # --- AGREGADO: Registro de Blueprints para los módulos ---
    from app.routes.auth import auth_bp
    from app.routes.finanzas import finanzas_bp
    from app.routes.inventario import inventario_bp
    from app.routes.pos import pos_bp
    from app.routes.qr_portal import qr_portal_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(finanzas_bp)
    app.register_blueprint(inventario_bp)
    app.register_blueprint(pos_bp)
    app.register_blueprint(qr_portal_bp)
    # --------------------------------------------------------

    # 3. Ruta raíz: Ahora manda directo al Login por seguridad
    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))

    # 4. Ruta principal conectada al Dashboard
    @app.route('/dashboard')
    def dashboard():
        from app.services.finanzas_manager import FinanzasManager
        
        # Llamamos al método correcto que tienes en tu clase
        resumen = FinanzasManager.calcular_balance_diario()
        
        return render_template(
            'admin/dashboard.html',
            total_ventas=resumen.get('ventas', 0.0),
            total_gastos=resumen.get('gastos', 0.0),
            balance_neto=resumen.get('balance_neto', 0.0)
        )

    return app