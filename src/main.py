""" Este scrip se encargaria de cargar un archivo cargado en
    Formato .dat para ser procesado y llevado a un formato mas
    legible que seria el formato excel"""

import pandas as pd
import openpyxl
import csv
import os
import datetime

class Operacion:
    def __init__(self,data = tuple()):
        self.__registro = data
    



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
    tipo_operacion = {'R' : 'Regular', 'P' : 'A Plazo', 'CC' : 'Cotizacion y Venta de Cierre'}
    with open('exit.csv','w') as archive_csv:
        # creamos el archivo exit.csv, montamos todos los datos en el csv
        for dato in datos:
            archive_csv.write(dato + ',')
        archive_csv.write('\n')

        with open(path,'r') as archive_dat:
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
        print(dataFrame)

        today = datetime.datetime.today()

        dataFrame.to_excel(f'{today.day}-{today.month}-{today.year}.xlsx')
        dataFrame_mejorado.to_excel(f'{today.day}-{today.month}-{today.year}(Rev).xlsx')
        

    # eliminamos el exit.csv
    if os.path.exists('exit.csv'):
        os.remove(
            'exit.csv'
        )
    
# def ganacia()

if __name__ == '__main__':
    procesar_excel('./input/diario.dat')