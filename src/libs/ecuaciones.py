# -*- coding: utf-8 -*-
from libs.pila import Pila
from libs.nodo import Nodo

class ArbolPosFijo:
    diccionario={}

    def evaluar(self, arbol):
        if arbol.valor=='+':
            return self.evaluar(arbol.izquierda)+self.evaluar(arbol.derecha)
        if arbol.valor=='-':
            return self.evaluar(arbol.izquierda)-self.evaluar(arbol.derecha)
        if arbol.valor=='*':
           return self.evaluar(arbol.izquierda)*self.evaluar(arbol.derecha)
        if arbol.valor=='/':
           return self.evaluar(arbol.izquierda)/self.evaluar(arbol.derecha)
        try:
           return int(arbol.valor)
        except:
          return (self.getValorDiccionario(arbol.valor))

    def addDiccionario(self,indice,valor):
        self.diccionario[indice]=valor

    def getValorDiccionario(self,indice):
        return self.diccionario.get(indice)

    def printDiccionario(self):
         for i in self.diccionario:
             print ("{} = {}".format(i,self.getValorDiccionario(i)))

    def construirPosfijo(self, posfijo):
        posfijo.pop()
        variable=posfijo.pop()
        pilaOperador = Pila()
        for caracter in posfijo :
            if (caracter == '+' or caracter == '-' or caracter == '*' or caracter == '/'):
                arbol = nodo.Nodo(caracter)
                arbol.derecha = pilaOperador.desapilar()
                arbol.izquierda = pilaOperador.desapilar()
                pilaOperador.apilar(arbol)
            else:
                arbol = nodo.Nodo(caracter)
                pilaOperador.apilar(arbol)

        arbol = pilaOperador.desapilar()
        self.addDiccionario(variable,self.evaluar(arbol))
        return self.evaluar(arbol)
