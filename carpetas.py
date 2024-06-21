import os

def crear_carpetas(ruta, nombres_carpetas):
    if not os.path.exists(ruta):
        os.makedirs(ruta)

    for nombre in nombres_carpetas:
        nueva_ruta = os.path.join(ruta, nombre)
        os.makedirs(nueva_ruta)
        print(f'Se ha creado la carpeta: {nueva_ruta}')

directorio_destino = r'ruta donde se crearán las carpetas'

nombres = [
    'Carpeta1',
    'Carpeta2',
    'Carpeta n'
]

crear_carpetas(directorio_destino, nombres)

"""
Alivia la carga de trabajo de creación de carpetas para un directorio con automatización
"""