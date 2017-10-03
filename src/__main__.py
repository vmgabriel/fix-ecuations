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

if __name__ == "__main__":
    # Ejercicio solucionar ecuaciones:
        #obj = ArbolPosFijo()
        #print("INGRESE LA O LAS ECUACIONES:")
        #while True:
        #    expresion = raw_input().split()
        #    if not expresion:
        #        print(" ==========  RESULTADO ==========  ")
        #        obj.printDiccionario()
        #        break
        #    obj.construirPosfijo(expresion)
        # ====================================================================

        # Ejercicio evaluar Tokens
        obj = ArbolPosFijo()
        error=0
        listaTipo = []
        listaValor = []
        print("INGRESE LA O LAS ECUACIONES:")
        while True:
            expresion = raw_input().split()
            if not expresion:
                print(" ==========  RESULTADO ==========  ")
                obj.printDiccionario()
                #obj.imprimirTabla(listaTipo,listaValor)
                break
            print (' '.join(expresion))
            error=obj.evaluarCaracteres(expresion, listaTipo, listaValor)
            if(error==0):
                print ("El valor resultado es: "+ str(obj.construirPosfijo(expresion)))
                obj.imprimirTabla(listaTipo,listaValor)
