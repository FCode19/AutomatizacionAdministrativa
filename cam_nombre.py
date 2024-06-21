import os

def cambiar_nombres(ruta_carpeta):
    if not os.path.isdir(ruta_carpeta):
        print(f"La ruta '{ruta_carpeta}' no es una carpeta válida.")
        return
    
    archivos = os.listdir(ruta_carpeta)
    
    numero = 279 #poner un numero o modificarlo por cadena
    
    for archivo in archivos:
        _, extension = os.path.splitext(archivo)
        
        nuevo_nombre = f"{numero}{extension}"
        
        ruta_anterior = os.path.join(ruta_carpeta, archivo)
        ruta_nueva = os.path.join(ruta_carpeta, nuevo_nombre)
        
        os.rename(ruta_anterior, ruta_nueva)
        
        numero += 1

    print("Nombres de archivos cambiados exitosamente.")

ruta_carpeta = r"ruta de carpeta donde estan los archivos a cambiar nombres"

cambiar_nombres(ruta_carpeta)

"""
Este pequeño programa es util para manejar gran volumen de archivos y tener nombres iterativos automatizando el proceso.
ejm: IMG_001, IMG_002,...
"""