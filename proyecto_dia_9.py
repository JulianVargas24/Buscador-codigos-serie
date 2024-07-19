import os
import re
import time
import datetime
from pathlib import Path
import math

inicio = time.time()


#Poner la ruta donde se encuentra carpeta "Mi_Gran_Directorio"
ruta = 'C:\\Users\\Julian\\Desktop\\Python\\pythonProject\\Dia 9\\Proyecto+Dia+9\\Mi_Gran_Directorio'
mi_patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
num_encontrados = []
arch_encontrados = []


def buscar_numero(archivo, patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''


def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta, a), mi_patron)
            if resultado != '':
                num_encontrados.append(resultado.group())
                arch_encontrados.append(a.title())


def mostrar_todo():
    indice = 0
    print('-' * 36)
    print(f'Fecha de Búsqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('Archivo\t\t\tNro. Serie')
    print('-------\t\t\t----------')
    for a in arch_encontrados:
        print(f'{a}\t{num_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Número encontrados: {len(num_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')
    print('-' * 36)


crear_listas()
mostrar_todo()