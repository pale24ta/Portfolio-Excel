""" Este scrip se encargaria de cargar un archivo cargado en
    Formato .dat para ser procesado y llevado a un formato mas
    legible que seria el formato excel"""

import pandas as pd
import openpyxl
import csv
import os
import datetime



def guardar_en_escritrorio(archivo_excel):
    if os.name == 'nt':  # Windows
        escritorio = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Escritorio')
        if escritorio is None:
            escritorio = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')       
    else:  # macOS y Linux
        escritorio = os.path.join(os.path.join(os.path.expanduser('~')), 'Escritorio')
        if escritorio is None:
            escritorio = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    ruta_completa = os.path.join(escritorio, archivo_excel)
    return ruta_completa

def procesar_excel(path):
    # el primer paso seria copiar los datos a un archivo .csv y luego manipular el .csv
    datos = ['Tipo de Operacion','Acciones',
                                  'Simbolo',
                                  'Precio De Cierre(Anterior)',
                                  'Precio De Cierre(Actual)',
                                  'Valor Absoluto'
                                  ,'Valor Re%'
                                  ,'Precio Bs.S(Min)',
                                  'Precio Bs.S(Max)',
                                  'Precio Bs.S Promedio',
                                  'No Operacion',
                                  'Cantiadad de Acciones',''
                                  'Monto Bs Negociable']

    with open('exit.csv','w', encoding = 'utf-8') as archive_csv:
        # creamos el archivo exit.csv, montamos todos los datos en el csv
        for dato in datos:
            archive_csv.write(dato + ',')
        archive_csv.write('\n')

        # abrir el archivo .dat con una codificación tolerante a caracteres locales
        # muchos archivos .dat/legacy usan latin-1/cp1252; usar 'errors=replace' evita excepciones
        with open(path, 'r', encoding='latin-1', errors='replace') as archive_dat:
            count = 1
            for line in archive_dat:
                if count  >= 4:
                    archive_csv.write(line.replace('|',','))
                count += 1
    
    # cargamos el csv como diccionario
    with open('exit.csv','r', encoding= 'utf-8') as archive_csv:
        dic = csv.DictReader(archive_csv)
        dataFrame = pd.DataFrame(columns=datos)

        for dato in dic:
            dataFrame.loc[len(dataFrame)] = dato
        

        # Etapa para procesar del dataFrame

        dataFrame_mejorado = dataFrame.drop(['Precio Bs.S(Min)','Precio Bs.S(Max)','No Operacion'],axis = 1)

        today = datetime.datetime.today()
    

        dataFrame.to_excel(guardar_en_escritrorio(f'Bolsa_Caracas_{today.day}-{today.month}-{today.year}.xlsx'))
        dataFrame_mejorado.to_excel(guardar_en_escritrorio(f'Bolsa_Caracas{today.day}-{today.month}-{today.year}(Rev).xlsx'))

        

    # eliminamos el exit.csv
    if os.path.exists('exit.csv'):
        os.remove(
            'exit.csv'
        )
    
# def ganacia()

from tkinter import Tk
from tkinter import filedialog,messagebox,dialog

if __name__ == '__main__':
    
    root = Tk()
    root.withdraw()

    ruta_principal = filedialog.askopenfile(title= "Seleccione el archivo .dat")
    ruta = ruta_principal.name
    ruta_principal.close()
    if not '.dat' in ruta:
        messagebox.askyesnocancel('Error','Archivo incorrecto')
    else:
        procesar_excel(ruta)
    # procesar_excel('./input/diario.dat')/home/brigido/Descargas/diario20251114.dat