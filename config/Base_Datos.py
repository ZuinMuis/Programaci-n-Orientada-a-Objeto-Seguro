import sqlite3
from pathlib import Path
from sqlite3 import Connection, Cursor

class Database:
    """
    Clase que gestiona la conexión a la base de datos implementando 
    el patrón Singleton para evitar múltiples instancias innecesarias.
    """
    _instance = None
    _db_path = str(Path(__file__).resolve().parent.parent / "sistema_gestion.db")

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def get_connection(self) -> Connection:
        """
        Retorna una conexión a la base de datos SQLite con soporte para nombres de columnas.
        """
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row  # Permite acceder a las columnas por nombre
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def init_db(self) -> None:
        """
        Inicializa la base de datos creando las tablas del diagrama UML 
        si no existen previamente.
        """
        conn = self.get_connection()
        try:
            cursor: Cursor = conn.cursor()          
            
            # 1. Tabla Departamento (Independiente)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS departamento (
                    id_departamento INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    gerente TEXT NOT NULL
                )
            """)

            # 2. Tabla Proyecto (Independiente)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS proyecto (
                    id_proyecto INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    descripcion TEXT NOT NULL,
                    fecha_inicio TEXT NOT NULL
                )
            """)

            # 3. Tabla Usuario (Clase base del UML)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuario (
                    id_usuario INTEGER PRIMARY KEY,
                    correo TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    rol TEXT NOT NULL,
                    id_departamento INTEGER,
                    FOREIGN KEY(id_departamento) REFERENCES departamento(id_departamento) ON DELETE SET NULL
                )
            """)

            # 4. Tabla Empleado (Especialización de Usuario con sus atributos propios)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS empleado (
                    id_empleado INTEGER PRIMARY KEY,
                    id_usuario INTEGER UNIQUE,
                    nombre TEXT NOT NULL,
                    direccion TEXT NOT NULL,
                    telefono TEXT NOT NULL,
                    email TEXT NOT NULL,
                    fecha_contrato TEXT NOT NULL,
                    salario REAL NOT NULL,
                    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE
                )
            """)

            # 5. Tabla Registro_Tiempo (Asociada a Empleado y Proyecto)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS registro_tiempo (
                    id_registro INTEGER PRIMARY KEY,
                    fecha TEXT NOT NULL,
                    horas REAL NOT NULL CHECK (horas > 0),
                    descripcion TEXT NOT NULL,
                    id_empleado INTEGER,
                    id_proyecto INTEGER,
                    FOREIGN KEY(id_empleado) REFERENCES empleado(id_empleado) ON DELETE CASCADE,
                    FOREIGN KEY(id_proyecto) REFERENCES proyecto(id_proyecto) ON DELETE CASCADE
                )
            """)
            
            conn.commit()
        finally:
            conn.close()

if __name__ == "__main__":
    db = Database()
    db.init_db()