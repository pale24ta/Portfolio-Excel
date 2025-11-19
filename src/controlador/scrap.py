import requests
import os
import datetime

""" Scrip que descarga el archivo .dat"""


def descargar_archivo_simple(url, nombre_archivo=None):
    """
    Descarga un archivo desde una URL (método simple)
    """
    try:
        # Headers para simular navegador
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Hacer la solicitud
        response = requests.get(url)
        response.raise_for_status()  # Lanza error si no es 200
        
        # Determinar nombre del archivo
        if not nombre_archivo:
            # Extraer nombre de la URL
            nombre_archivo = os.path.basename(url)
            if not nombre_archivo or '.' not in nombre_archivo:
                nombre_archivo = 'archivo_descargado.dat'
        
        # Guardar el archivo
        with open(nombre_archivo, 'wb') as archivo:
            archivo.write(response.content)
        
        # Verificar tamaño

        tamaño = os.path.getsize(nombre_archivo)
        if tamaño > 0:
            print(f"✅ Descargado: {nombre_archivo} ({tamaño} bytes)")
            return nombre_archivo
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error en la descarga: {e}")
        return None

# Ejemplo de uso


def descargar_diario_actual():
     # primero pasamos la fecha a carateres legibles para el url
    dia_actual_normal =  datetime.datetime.now()

    # contador hasta 6 dias anteriores
    count = 6
    url = 'https://www.bolsadecaracas.com/descargar-diario-bolsa/?type=dat&fecha='

    while count > 0:

        # cargamos la cadena del dia
        cadena = dia_actual_normal.strftime('%Y%m%d')
        
        # descargamos archivo
        archivo = descargar_archivo_simple(url + cadena,cadena + '.dat')
        print(url + cadena)
        
        # si el archivo fue descargado exitsamente
        if archivo:
            break

        # seguimos probando
        dia_actual_normal = dia_actual_normal - datetime.timedelta(days=1)
        count -= 1
    
    # no hubo exito
