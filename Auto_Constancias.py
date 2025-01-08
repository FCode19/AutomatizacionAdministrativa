from docx import Document
import os

# Rutas
ruta_origen = r""#Ruta inicial de documento de referencia
ruta_destino = r""#Ruta final de documento ya transformado

# Lista de nombres (para este caso), usar otros atributos según sea necesario
nombres = [
    #En este espacio llenar el contenido a utilizar
]


# Función para reemplazar texto y mantener formato
def reemplazar_texto(parrafo, texto_a_reemplazar, nuevo_texto):
    for run in parrafo.runs:
        if texto_a_reemplazar in run.text:
            # Reemplazar texto
            run.text = run.text.replace(texto_a_reemplazar, nuevo_texto)
            # Configurar formato
            run.font.bold = True
            run.font.name = "Arial Rounded MT Bold"
            run.text = run.text.upper()  # Convertir a mayúsculas

# Crear documentos personalizados
for nombre in nombres:
    # Abrir el documento modelo
    doc = Document(os.path.join(ruta_origen, "MODELO CONSTANCIA DE VACANTE Y REQUISTOS.docx"))
    
    # Buscar y reemplazar <<NOMBRE>> con el nombre actual
    for parrafo in doc.paragraphs:
        reemplazar_texto(parrafo, "<<NOMBRE>>", nombre)
    
    # Guardar el nuevo documento con el nombre específico
    nombre_archivo = f"CONSTANCIA DE VACANTE Y REQUISITOS_{nombre}.docx"#Se le puede cambiar según el caso sea necesario si se desea con otros atributos
    doc.save(os.path.join(ruta_destino, nombre_archivo))
