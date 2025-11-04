import sqlite3
import csv
from estudiante import estudiante

class GestorBaseDatos:
    def __init__(self, nombre_bd: str = "estudiantes.db"):
        self.nombre_bd = nombre_bd

    def crear_base(self) -> None:
        conn = sqlite3.connect(self.nombre_bd)
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF  NOT EXISTS estudiantes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,            
            nombre TEXT NOt NULL,
            correo TEXT NOT NULL UNIQUE,
            nota REAL
        )

        """)
        conn.commit()
        conn.close()
        print(f"[ok] Base de datos{self.nombre_bd} creada y en funcionamiento")

    def importar_datos ( csv_file : str , nombre_bd : str = "estudiantes.db")-> None :
       
        conn = sqlite3.connect(nombre_bd)
        cur = conn.cursor()
        with open ( csv_file , newline ='', encoding ='utf -8 ') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                try:
                    cur.execute (
                        " INSERT INTO estudiantes ( nombre , correo , nota ) VALUES (? , ?, ?)",
                        (fila['nombre'], fila ['correo'], float(fila ['nota'
                            ]))
                    )
                except sqlite3.IntegrityError:
                    print(f"[ ADVERTENCIA ] Registro duplicado: { fila ['correo']}")

        conn.commit()
        conn.close ()
        print("[OK] Registros importados correctamente")
    

    def contar_estudiantes(self) -> tuple:
        conn = sqlite3.connect(self.nombre_bd)
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM estudiantes")
        cantidad = cur.fetchone()[0]
        conn.close()
        return cantidad
    
    def actualizar_estudiantes(self, nombre:str, correo:str, nueva_nota:float)->None:
        conn = sqlite3.connect(self.nombre_db)
        cur = conn.cursor()
        try:
            cur.execute("UPDATE estudiantes SET nota = ? WHERE nombre = ? WHERE correo = ?",(nueva_nota,nombre,correo))
        except sqlite3.IntegrityError:
            print("[ADVERTENCIA] Actualizacion de estudiante no completada satisfactoriamente")
        conn.commit()
        conn.close()
        print("[ok]Actualizacion de datos de estudiante finalizada correctamente")

    def borrar_estudiantes(self, umbral: float = 3.5) -> None:
        conn = sqlite3.connect(self.nombre_bd)
        cur = conn.cursor()
        try:
            cur.execute("DELETE FROM estudiantes WHERE nota <?",{umbral,})
        except sqlite3.IntegrityError:
            print("[ADVERTENCIA] intento de borrado de informacion no completado satisfactoriamente")
        conn.commit
        conn.close()
        print("[OK]Estudiantes borrados correctamente")

    def listar_estudiantes(self) -> list[estudiante]:
        conn = sqlite3.connect(self.nombre_bd)
        cur = conn.cursor()
        cur.execute("SELECT nombre, corre, nota FROM estudiantes")
        filas = cur.fetchall()
        conn.close
        return [estudiante(nombre, correo, nota) for nombre, correo, nota in filas]
    
    def agregar_estudiante(self, estudiante : estudiante) -> None:
        conn = sqlite3.connect(self.nombre_bd)
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO estudiantes (nombre, correo, nota) VALUES (?, ?, ?)", (estudiante.nombre, estudiante.correo, estudiante.nota))
        except sqlite3.IntegrityError:
            print("[Advertencia] proceso de agregado de estudiante interrumpida")
        conn.commit()
        conn.close()

    def buscar_xnombre(self, nombre:str) -> list[estudiante]:
        conn = sqlite3.connect(self.nombre_bd)
        cur = conn.cursor()
        cur.execute("SELECT * FROM estudiantes WHERE nombre LIKE ?",(f"%{nombre}%",))
        filas = cur.fetchall()
        conn.close()
        return [estudiante(nombre, correo, nota)for nombre, correo, nota in filas]