class VistaConsola:
    @staticmethod
    def mostrar_menu(self) -> None:
        print("\n______Menu gestor de estudiantes______")
        print("1. Agregar estudiantes")
        print("2. Listar estudiantes")
        print("3. Actulizar nota")
        print("4. eliminar registro")
        print("5. busqueda por nombre")
        print("6. salir")

    def mostrar_estudiantes(resultados: list, umbral: float):
        print(f"\n[info] estudiantes con nota >= {umbral}")
        print("___________________________________________")
        for nombre, nota in resultados:
            print(f"{nombre:10s} | {nota:.2f}")

    @staticmethod
    def mostrar_mensaje(mensaje:str):
        print(mensaje)

    def pedir_datos_estudiante(self) -> tuple:
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        nota = float(input("Nota: "))
        return nombre, correo, nota
    
    
    def pedir_nombre0caracter(self) -> str:
        nombre = input("ingrese el nombre o caracter por el cual desea buscar: ")
        return nombre

    def pedir_actualizacion(self) -> tuple:
        nombre = input("nombre del estudiante a actualizar")
        correo = input("Correo del estudiante a actualizar: ")
        nueva_nota = float(input("Nueva nota: "))
        return nombre, correo, nueva_nota
    
    def pedir_umbral_eliminar(self) -> float:
        return input("hasta que nota los estudiantes se eliminan: ")
    
    def mostrar_listaEstudiantes(self, estudiantes: list):
        print("\n__________lista de estudiantes__________")
        for e in estudiantes:
            print(f"{e.nombre:10} | {e.correo:20} | Nota: {e.nota:.1f}")


