class estudiante:
    def __init__(self, nombre, correo, nota):
        self.nombre = nombre.strip()
        self.correo = correo.strip()
        self.nota = nota

    def __repr__(self):
        return f"Estudiantes(nombre='{self.nombre}', correo = '{self.correo}', nota = '{self.nota}')"
