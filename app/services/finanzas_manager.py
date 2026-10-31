from datetime import date
from sqlalchemy import func
from app import db
# Ajusta las importaciones según los nombres exactos de tus modelos en app/models
from app.models import Gasto, Venta, Compra  # Si 'Venta' o 'Compra' tienen otro nombre, me avisas

class FinanzasManager:
    
    @staticmethod
    def calcular_balance_diario(fecha_objetivo=None):
        """Calcula el balance financiero para una fecha específica (por defecto, hoy)."""
        if not fecha_objetivo:
            fecha_objetivo = date.today()
            
        # Total de ventas del día
        total_ventas = db.session.query(func.coalesce(func.sum(Venta.total), 0)).filter(
            func.date(Venta.fecha_hora) == fecha_objetivo
        ).scalar()
        
        # Total de gastos del día
        total_gastos = db.session.query(func.coalesce(func.sum(Gasto.valor), 0)).filter(
            func.date(Gasto.fecha_hora) == fecha_objetivo
        ).scalar()
        
        # Total de compras a proveedores del día
        total_compras = db.session.query(func.coalesce(func.sum(Compra.total), 0)).filter(
            func.date(Compra.fecha_hora) == fecha_objetivo
        ).scalar()
        
        # Balance neto (Ingresos - (Gastos + Compras))
        balance_neto = total_ventas - (total_gastos + total_compras)
        
        return {
            "fecha": str(fecha_objetivo),
            "ventas": float(total_ventas),
            "gastos": float(total_gastos),
            "compras": float(total_compras),
            "balance_neto": float(balance_neto)
        }

    @staticmethod
    def calcular_balance_mensual(anio: int, mes: int):
        """Calcula el balance financiero para un mes y año específico."""
        total_ventas = db.session.query(func.coalesce(func.sum(Venta.total), 0)).filter(
            func.extract('year', Venta.fecha_hora) == anio,
            func.extract('month', Venta.fecha_hora) == mes
        ).scalar()
        
        total_gastos = db.session.query(func.coalesce(func.sum(Gasto.valor), 0)).filter(
            func.extract('year', Gasto.fecha_hora) == anio,
            func.extract('month', Gasto.fecha_hora) == mes
        ).scalar()
        
        total_compras = db.session.query(func.coalesce(func.sum(Compra.total), 0)).filter(
            func.extract('year', Compra.fecha_hora) == anio,
            func.extract('month', Compra.fecha_hora) == mes
        ).scalar()
        
        balance_neto = total_ventas - (total_gastos + total_compras)
        
        return {
            "anio": anio,
            "mes": mes,
            "ventas": float(total_ventas),
            "gastos": float(total_gastos),
            "compras": float(total_compras),
            "balance_neto": float(balance_neto)
        }

    @staticmethod
    def calcular_balance_anual(anio: int):
        """Calcula el balance financiero global para todo el año."""
        total_ventas = db.session.query(func.coalesce(func.sum(Venta.total), 0)).filter(
            func.extract('year', Venta.fecha_hora) == anio
        ).scalar()
        
        total_gastos = db.session.query(func.coalesce(func.sum(Gasto.valor), 0)).filter(
            func.extract('year', Gasto.fecha_hora) == anio
        ).scalar()
        
        total_compras = db.session.query(func.coalesce(func.sum(Compra.total), 0)).filter(
            func.extract('year', Compra.fecha_hora) == anio
        ).scalar()
        
        balance_neto = total_ventas - (total_gastos + total_compras)
        
        return {
            "anio": anio,
            "ventas": float(total_ventas),
            "gastos": float(total_gastos),
            "compras": float(total_compras),
            "balance_neto": float(balance_neto)
        }