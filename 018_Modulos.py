


# Módulos

"""
Para llamar a una función que tengamos en un módulo tenemos que importarla y luego 
usar la nomenclatura del punto:
Suponiendo que en un módulo funciones.py tenemos la siguiente función suma:
"""
def suma(num1, num2):
    print("suma= ", num1+num2)
    
#   Desde otro módulo la llamaríamos así:

import funciones
funciones.suma(3,4)	#Además de importar debemos usar la nomenclatura del punto.


#   Para simplificar también podemos poner:

from funciones import suma
suma(3,4)

#   De esta forma, además, ya no necesitamos usar la nomenclatura del punto.

# ---------------------------------------


#   Si queremos importar todo el contenido de un paquete:

from funciones import *

#   La función dir() enumera todos los elementos de un módulo. 

import funciones

x = dir(funciones)
print(x)
2400

"""
1. Importar y renombrar un módulo
Puedes renombrar un módulo al importarlo, lo que es útil si quieres usar un nombre más corto o más significativo.
"""
Python
import funciones as f

f.suma(5, 7)  # Usamos el alias 'f' para llamar a la función
"""
2. Importar varias funciones específicas
Puedes importar múltiples funciones de un módulo directamente.
"""
Python
from funciones import suma, resta

suma(8, 3)  # Llama a la función suma
resta(10, 4)  # Llama a la función resta
"""
3. Uso de un módulo estándar de Python
Python tiene muchos módulos estándar que puedes usar sin necesidad de instalarlos. Por ejemplo, el módulo math:
"""
Python
import math

resultado = math.sqrt(16)  # Calcula la raíz cuadrada
print("Raíz cuadrada:", resultado)
"""
4. Crear un módulo personalizado
Puedes crear tu propio módulo (por ejemplo, operaciones.py) y luego importarlo en otro archivo.
"""
Archivo: operaciones.py

Python
def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"
Archivo principal:

Python
import operaciones

print(operaciones.multiplicar(6, 7))
print(operaciones.dividir(10, 2))
"""
5. Importar submódulos de un paquete
Si tienes un paquete estructurado con submódulos, puedes importarlos individualmente.

Estructura de directorios:
"""
Code
mi_paquete/
    __init__.py
    modulo1.py
    modulo2.py
Código:

Python
from mi_paquete import modulo1, modulo2

modulo1.funcion1()
modulo2.funcion2()
