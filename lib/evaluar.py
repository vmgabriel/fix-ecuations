#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nodo import Nodo

class evaluarExpresion:
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
        
