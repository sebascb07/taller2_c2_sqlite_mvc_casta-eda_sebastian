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