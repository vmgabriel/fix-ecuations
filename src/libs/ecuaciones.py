# -*- coding: utf-8 -*-

from libs.pila import Pila
from libs.nodo import Nodo

class ArbolPosFijo:
    diccionario={}
    lista=[]
    arbol=None

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

    def addListaTipo(self,indice,valor):
        self.lista.append([indice,valor])

    def getValorDiccionario(self,indice):
        return self.diccionario.get(indice)

    def printDiccionario(self):
         for i in self.diccionario:
             print ("{} = {}".format(i,self.getValorDiccionario(i)))

    def printListaTipo(self):
        for i in self.lista:
            print ("{} -> {}".format(i[0],i[1]))

    def construirPosfijo(self, posfijo):
        posfijo.pop()
        variable=posfijo.pop()
        pilaOperador = Pila()
        for caracter in posfijo :
            if (caracter == '+' or caracter == '-' or caracter == '*' or caracter == '/' or caracter == "="):
                self.arbol = Nodo(caracter)
                self.arbol.derecha = pilaOperador.desapilar()
                self.arbol.izquierda = pilaOperador.desapilar()
                pilaOperador.apilar(self.arbol)

            else:
                self.arbol = Nodo(caracter)
                pilaOperador.apilar(self.arbol)

        self.arbol = pilaOperador.desapilar()
        self.addDiccionario(variable,self.evaluar(self.arbol))
        return self.evaluar(self.arbol)

    def construirPosfijoTabla(self,posfijo):
        for caracter in posfijo:
            if not (caracter.isalnum()):
                self.addListaTipo("Ope",caracter)
            elif (caracter.isdigit()):
                self.addListaTipo("Val",caracter)
            else:
                self.addListaTipo("Var",caracter)
