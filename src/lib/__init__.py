#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.nodo import Nodo

class evaluarExpresion:
    """Clase enfocada en las utilidades que el sistema necesita..."""
    def __init__(self):
        pass

    def evaluar(self, arbol):
        if arbol.valor=="+":
            return self.evaluar(arbol.izq)+self.evaluar(arbol.der)
        if arbol.valor=="-":
            return self.evaluar(arbol.izq)-self.evaluar(arbol.der)
        if arbol.valor=="*":
            return self.evaluar(arbol.izq)*self.evaluar(arbol.der)
        if arbol.valor=="/":
            return self.evaluar(arbol.izq)/self.evaluar(arbol.der)
        return int(arbol.valor)

    def cantLetras(self,arbol):
        cant=0
        if not (arbol == []):
            if ((type(arbol.valor)==str) and (arbol.valor != "+" or
            arbol.valor != "-" or arbol.valor != "*" or arbol.valor != "/" or
             arbol.valor != "=")):
                cant+=1
        return self.cantLetras(arbol.izq)+self.cantLetras(arbol.der)+cant
