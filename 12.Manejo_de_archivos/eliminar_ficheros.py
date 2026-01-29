import os

# Eliminando ficheros o archivos
if os.path.exists("prueba.txt"):
    os.remove("prueba.txt")
else:
    print("El archivo que intenta eliminar no existe")

# Eliminando carpetas
os.rmdir("prueba")

#Eliminando carpeta método serio
import shutil
import os
import stat

def eliminar_force(path):
    def onerror(func, path, exc_info):
        os.chmod(path, stat.S_IWRITE)
        func(path)

    shutil.rmtree(path, onerror=onerror)

eliminar_force("prueba")

