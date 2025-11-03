class estudiante:
    def __init__(self, nombre, correo, nota):
        self.nombre = nombre
        self.correo = correo
        self.nota = nota

    def __repr__(self):
        return f"Estudiantes(nombre='{self.nombre}', correo = '{self.correo}', nota = '{self.nota}')"
