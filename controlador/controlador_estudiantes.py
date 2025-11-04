from pathlib import Path
from modelo.gestor_csv import GestorCSV
from modelo.gestor_bd import GestorBaseDatos
from vista.vista_consola import VistaConsola

class gestorEstudiantes:
    def __init__(self):
        self.bd = GestorBaseDatos()
        self.csv = GestorCSV()
        self.vista = VistaConsola()

    def inicializar_datos_base(self):
        ruta_base = Path("estudiantes.db")
        ruta_csv = Path("estudiantes.csv")
        if not ruta_base.exists():
            print("base de datos inicializada")
        else:
            print("base de datos encontrada")
        if not ruta_csv.exists():
            GestorCSV.generar_csv()
        else:
            print("archivo csv inicial encontrado")
        if self.bd.contar_estudiantes() == 0:
            self.bd.importar_datos("estudiantes.csv")
        else:
            print("base de datos inicializada en estado original correctamente")
            


    
