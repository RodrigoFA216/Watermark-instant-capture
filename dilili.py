import os
import mimetypes


def obtener_tipo_archivo(extension):
    mime_type, _ = mimetypes.guess_type(f"archivo.{extension}")
    return mime_type or "Desconocido"


def listar_archivos(ruta):
    for dirpath, dirnames, filenames in os.walk(ruta):
        for archivo in filenames:
            nombre, extension = os.path.splitext(archivo)
            tipo = obtener_tipo_archivo(extension.lstrip("."))
            ruta_completa = os.path.join(dirpath, archivo)
            print(f"Archivo: {ruta_completa}, Tipo: {tipo}")


if __name__ == "__main__":
    carpeta_base = r"Este equipo/Galaxy Tab A/Tablet"

    if os.path.exists(carpeta_base):
        listar_archivos(carpeta_base)
    else:
        print("La carpeta especificada no existe.")
