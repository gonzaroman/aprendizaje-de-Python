
#modulos de python
#listado de modulos:
#https://docs.python.org/3/py-modindex.html
#modulos descargados de internet
#https://pypi.org/
#nuestros modulos


#nos podemos traer todo el modulo con los metodos,entonces se llama desde datetime.loquesea
import datetime

print(datetime.date.today()) #llamamos a datetime y luego los metodos

print(datetime.timedelta(minutes=90))


#llamamos solo a los metodos que queremos
from datetime import timedelta, date

print(date.today) #llamamos directamente a los metodos, no hace falta  poner datetime

print(timedelta(minutes=90))


#llamamos al modulo que hemos creado mimodulocreado.py

import mimodulocreado

mimodulocreado.suma(3,23)
mimodulocreado.resta(10,6)

from mimodulocreado import suma, resta
suma(20,34)
resta(40,3)

#modulos descargados de  internet
#nos vamos a la pagina pypi.org y buscamos el modulo que queremos
#vamos a usar colorama
#lo instalamos en la terminal con:
#pip install colorama

#import colorama
from colorama import Fore, Style

print(Fore.GREEN+"texto escrito con colorama")