import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import shutil

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "diligencia")
        algorithm_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "algoritmo")
        # Nombre de la imagen recién añadida
        new_image_name = os.path.basename(event.src_path)
        # Si la imagen recién añadida no contiene '-s' en el nombre
        if '-s' not in new_image_name:
            # Mover la imagen recién añadida a la carpeta "algoritmo"
            shutil.move(os.path.join(folder_path, new_image_name), os.path.join(algorithm_folder_path, new_image_name))
            print(f"Imagen {new_image_name} movida a la carpeta 'algoritmo'")
            # Ruta completa de la imagen "blur.jpeg"
            blur_image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "blur.jpeg")
            # Construir el nuevo nombre para la imagen "blur.jpeg" en la carpeta "diligencia"
            new_blur_image_name = os.path.splitext(new_image_name)[0] + "-s" + os.path.splitext(blur_image_path)[1]
            # Copiar la imagen "blur.jpeg" a la carpeta "diligencia" con el nuevo nombre
            shutil.copy(blur_image_path, os.path.join(folder_path, new_blur_image_name))
            print(f"Imagen blur.jpeg copiada y renombrada a {new_blur_image_name} en la carpeta 'diligencia'")

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "diligencia")
    observer.schedule(event_handler, folder_path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
