import psycopg
from psycopg import sql

def crear_base_de_datos():
    # Cambia 'TU_CONTRASEÑA' por la clave que le asignaste a tu usuario postgres
    conn_info = "dbname=postgres user=postgres password=3213477253duber host=localhost port=5432"
    
    try:
        conn = psycopg.connect(conn_info, autocommit=True)
        cursor = conn.cursor()
        
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'miscelia_db'")
        exists = cursor.fetchone()
        
        if not exists:
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier("miscelia_db")))
            print("¡Base de datos 'miscelia_db' creada exitosamente en PostgreSQL!")
        else:
            print("La base de datos 'miscelia_db' ya existe en PostgreSQL.")
            
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error conectando a PostgreSQL: {e}")

if __name__ == "__main__":
    crear_base_de_datos()