#!/urs/bin/env python
# -*- coding: utf-8 -*-

"""
Archivo para Metodo principal

@author: Andres Aguirre - Dalia Muñoz - Gabriel Vargas
@version: 0.1
@license: GPL
@contact: vmgabriel96@gmail.com
"""

from cli import Cli
from libs.ecuaciones import ArbolPosFijo

# Ejercicio:
obj = ArbolPosFijo()
print("INGRESE LA O LAS ECUACIONES:")
while True:
    expresion = input().split()
    if not expresion:
        print(" ==========  RESULTADO ==========  ")
        obj.printDiccionario()
        break
    obj.construirPosfijo(expresion)
