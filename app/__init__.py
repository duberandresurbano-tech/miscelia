from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 1. Primero inicializamos las extensiones con la app
    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.usuario import Rol, Usuario, usuario_rol
    from app.models.producto import Categoria, Producto, PresentacionProducto
    from app.models.proveedor import Proveedor, Compra, DetalleCompra
    from app.models.venta import Venta, DetalleVenta, HistorialCorreccionVenta
    from app.models.inventario import MovimientoInventario
    from app.models.pedido_qr import PedidoQR, DetallePedidoQR, Gasto

    # 3. Ruta de prueba temporal para verificar que enciende
    @app.route('/')
    def index():
        return "¡Miscelia Backend funcionando al 100%! 🚀"

    return app