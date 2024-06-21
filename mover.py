import os
import shutil

def copiar_archivos_a_carpetas(ruta_origen, ruta_destino):
    archivos_excel = [archivo for archivo in os.listdir(ruta_origen) if archivo.endswith('.xlsx')]

    for carpeta in os.listdir(ruta_destino):
        carpeta_ruta = os.path.join(ruta_destino, carpeta)
        if os.path.isdir(carpeta_ruta):
            for archivo_excel in archivos_excel:
                ruta_archivo_origen = os.path.join(ruta_origen, archivo_excel)
                ruta_archivo_destino = os.path.join(carpeta_ruta, archivo_excel)
                shutil.copy(ruta_archivo_origen, ruta_archivo_destino)
                print(f'Se ha copiado {archivo_excel} en {carpeta_ruta}')

directorio_destino = r'ruta de destino'

directorio_origen = r'ruta de origen'

copiar_archivos_a_carpetas(directorio_origen, directorio_destino)

"""
Permitirá hacer un recorrido en un directorio insertando archivos en cada carpeta
"""