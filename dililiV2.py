import os
import mimetypes
import sys

def obtener_tipo_archivo(extension):
    mime_type, _ = mimetypes.guess_type(f"archivo.{extension}")
    return mime_type or "Desconocido"

def listar_archivos(ruta, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        sys.stdout = f  # Redirigir la salida estándar al archivo

        for dirpath, dirnames, filenames in os.walk(ruta):
            for archivo in filenames:
                nombre, extension = os.path.splitext(archivo)
                tipo = obtener_tipo_archivo(extension.lstrip("."))
                ruta_completa = os.path.join(dirpath, archivo)
                print(f"Archivo: {ruta_completa}, Tipo: {tipo}")

if __name__ == "__main__":
    carpeta_base = r"C:/"
    output_file = os.path.join(carpeta_base, "results.txt")

    if os.path.exists(carpeta_base):
        listar_archivos(carpeta_base, output_file)
        print(f"Resultados guardados en: {output_file}")
    else:
        print("La carpeta especificada no existe.")
