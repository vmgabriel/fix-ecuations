# -*- coding: utf-8 -*-
from libs.pila import Pila
from libs.nodo import Nodo
import re

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
                arbol = Nodo(caracter)
                arbol.derecha = pilaOperador.desapilar()
                arbol.izquierda = pilaOperador.desapilar()
                pilaOperador.apilar(arbol)
            else:
                arbol = Nodo(caracter)
                pilaOperador.apilar(arbol)

        arbol = pilaOperador.desapilar()
        self.addDiccionario(variable,self.evaluar(arbol))
        return self.evaluar(arbol)

    def imprimirTabla(self,a1 , a2):
        a = 0
        for m in a1:
            print(a1[a] + "   " + a2[a])
            a = a+1
        print("====================================")


    def evaluarCaracteres(self, aux, l1 , l2):
        errores = 0
        for x in aux:
            if re.match('^[-+]?[0-9]+$', x):
                l1.append("Num")
                l2.append(x)
            elif re.match('[-|=|+|*|/]', x):
                l1.append("Oper")
                l2.append(x)
            elif re.match('^[a-zA-Z_][a-zA-Z0-9_]*$', x):
                l1.append("Var")
                l2.append(x)
            else:
                l1.append("TOKEN NO VALIDO")
                l2.append(x)
                errores+=1
        return errores
