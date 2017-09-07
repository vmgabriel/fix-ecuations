#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.nodo import Nodo

"""
Archivo basico de lib, tiene las propiedades de ser la fechaada de B{LIB}

@author: Andres Aguirre - Dalia Muñoz - Gabriel Vargas
@version: 0.1
@license: GPL
@contact: vmgabriel96@gmail.com
"""

class Funcionalidades:
    """Clase enfocada en las utilidades que el sistema necesita..."""
    def __init__(self):
        """Inicializador basico no tiene ninguna funcion apaarte"""
        pass

    def evaluar(self, arbol):
        """
        Evalua los datos de un arbol, retorna el resultado, metodo recursivo

        @param arbol: Arbol que se va a evaluarExpresion
        @type arbol: Nodo()
        @return: Valor del arbol que se hace al proceder
        @rtype: int
        """
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
        """
        Verifica la cantidad de letras de un arbol, si las tiene

        @param arbol: Arbol que se va a evaluarExpresion
        @type arbol: Nodo()
        @return: La cantidad de letras que tiene el arbol
        @rtype: int
        """
        cant=0
        if not (arbol == []):
            if ((type(arbol.valor)==str) and (arbol.valor != "+" or
            arbol.valor != "-" or arbol.valor != "*" or arbol.valor != "/" or
             arbol.valor != "=")):
                cant+=1
        return self.cantLetras(arbol.izq)+self.cantLetras(arbol.der)+cant

    def convertirPos(self,expresion):
        """
        Funcion(Metodo) basico para el uso de convertir los datos introducidos
        por el usuario a arbol, este si puede mantenerse

        @param expresion: Arreglo de datos que introdujo el usuario posordenado
        @type expresion: str[]
        @return: Arbol
        @rtype: Nodo()
        """
        pilaTemp = Pila()
        contador=0
        while (contador < len(expresion)):
            if (expresion[contador]=='+' or expresion[contador]=='-' or expresion[contador]=='*' or expresion[contador]=='/'):
                dato1=expresion.pop(contador-1)
                dato2=expresion.pop(contador-2)
                contador-=2
                expresion[contador]=Nodo(expresion[contador],dato2,dato1)
            else:
                expresion[contador]=Nodo(expresion[contador],None,None)
            contador+=1
        return expresion[0]

    def convertirPre(self,lista):
        """
        Funcion(Metodo) basico para el uso de convertir los datos introducidos
        por el usuario a arbol, este si puede mantenerse

        @param lista: Arreglo de datos que introdujo el usuario preordenado
        @type lista: str[]
        @return: Arbol
        @rtype: Nodo()
        """
	    x = len(lista)-1
	    pila1 = pila.Pila()
	    while x>=0:
	        nodo1 = Nodo(lista[x], None, None)
	        if nodo1.valor == "+" or nodo1.valor == "-" or nodo1.valor == "/" or nodo1.valor == "*" or nodo1.valor == "=":
	            raiz = nodo1
	            raiz.izq = pila1.desapilar()
	            raiz.der = pila1.desapilar()
	            pila1.apilar(raiz)
	        else:
	            pila1.apilar(nodo1)
	        x = x-1
	    while len(pila1.items)>0:
	        raiz = pila1.desapilar()
	        if pila1.es_vacia:
	            return raiz
	        if pila1.es_vacia == False:
	            raiz.izq = pila1.desapilar()
	        if pila1.es_vacia == False:
	            raiz.der = pila1.desapilar()
	        if pila1.es_vacia:
	            return raiz
