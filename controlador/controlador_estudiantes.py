from pathlib import Path
from modelo.estudiante import estudiante
from modelo.gestor_csv import GestorCSV
from modelo.gestor_bd import GestorBaseDatos
from vista.vista_consola import VistaConsola

class controladorEstudiantes:
    def __init__(self):
        self.bd = GestorBaseDatos()
        self.csv = GestorCSV()
        self.vista = VistaConsola()

    def inicializar_base_datos(self):
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
        
    def ejecutar_programa(self):
        while True:
            opcion = self.vista.mostrar_menu()

            if opcion == 1:
                datos = self.vista.pedir_datos_estudiante()
                estudiante = estudiante(*datos)
                self.bd.agregar_estudiante(estudiante)
                self.vista.mostrar_mensaje("Estudiante creado correctamente")
            

            elif opcion == 2:
                estudiantes = self.bd.listar_estudiantes()
                self.vista.mostrar_listaEstudiantes(estudiantes)

            
            elif opcion == 3:
                nombre, correo, nueva_nota = self.vista.pedir_actualizacion()
                self.bd.actualizar_estudiantes(nombre, correo, nueva_nota)
            

            elif opcion == 4:
                umbral = self.vista.pedir_umbral_eliminar()
                self.bd.borrar_estudiantes(umbral)


            elif opcion == 5:
                nombre = self.vista.pedir_nombre0caracter()
                self.vista.mostrar_mensaje(f"estos fueron los estudiantes encontrados con la busqueda: {nombre}")
                self.bd.buscar_xnombre(nombre)
            
            elif opcion == 6:
                self.vista.mostrar_mensaje("adios usuario")
                break
            else:
                self.vista.mostrar_mensaje("opcion invalida ingresada")
