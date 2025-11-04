from controlador.controlador_estudiantes import controladorEstudiantes

if __name__ == "__main__":
    app = controladorEstudiantes()
    app.inicializar_base_datos()
    app.ejecutar_programa()