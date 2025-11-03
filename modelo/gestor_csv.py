import csv

class GestarCSV:
    @staticmethod
    def generar_csv(nombre_archivo: str = "estudiantes.csv")-> None:
        datos = [
            ["nombre", "correo", "nota"],
            ["ana,","ana@gmail.com",4,5],
            ["luis","luis@gmail.com",3.8],
            ["sara","sara@gmail.com",4.2]
        ]
        with open(nombre_archivo, "w", newline='',encoding="utf-8") as f:
            csv.writer(f).writerows(datos)
        print(f"[ok] Archivo {nombre_archivo} generado correctamente")