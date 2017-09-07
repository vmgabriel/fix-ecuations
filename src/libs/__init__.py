#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pila import Pila
from nodo import Nodo
from cola import Cola

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
        """Inicializador basico no tiene ninguna funcion aparte"""
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
            if (expresion[contador]=='+' or expresion[contador]=='-' or
            expresion[contador]=='*' or expresion[contador]=='/' or expresion[contador]=="="):
                dato1=expresion.pop(contador-1)
                dato2=expresion.pop(contador-2)
                contador-=2
                expresion[contador]=Nodo(expresion[contador],dato2,dato1)
                print(expresion)
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
            x -=1
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

    def letraEsta(self,arbol,letra):
        """
        Reviza si la letra esta en el arbol

        @param arbol: Arbol en el que se va a evaluar
        @param letra: Letra a buscar
        @type arbol: Nodo()
        @type letra: str
        @return: Retorna True si el arbol contiene la letras
        @rtype: bool
        """
        if (arbol == None):
            return false;
        if (arbol.valor == letra):
            return true;
        return LetraDerecha(arbol.izq,letra) or LetraDerecha(arbol.der,letra)

    def convertir(self,nodo):
        """
        Convierte el valor del nodo.valor dejando la los arboles tanto izquierdo
        como derecho quietos

        @param nodo: Nodo a convertir, es un arbol...
        @type nodo: Nodo()
        @return: Retorna un arbol con el valor del signo cambiado, del resto quieto
        @rtype: Nodo()
        """
        cambio = ""
        if (nodo.valor == "+"):
            cambio = "-"
        if (nodo.valor == "-"):
            cambio = "+"
        if (nodo.valor == "*"):
            cambio ="/"
        if (nodo.valor == "/"):
            cambio="*"
        return Nodo(cambio,nodo.izq,nodo.der)

    def cruzar(self,arbol):
        """
        Cruza el arbol izquierdo con el derecho dejandolos viendo de manera opuesta

        @param arbol: Arbol al cual vamos a cruzar
        @type arbol: Nodo()
        @return: Arbol Cruzado
        @rtype: Nodo()
        """
        temp=arbol.der
        arbol.der=arbol.izq
        arbol.izq=temp
        return arbol

    def despejar(self,arbol,letra):
        """
        Metodo de alta funcionalidad recursivo y que posee una cantidad de herramientas
        internas su funcionalidad es complicada ya que se implemento como un algoritmo de
        fuerza bruta para cualquier tipo de arbol que tenga la herramienta::

                      (=)      Resuelve Despejando A
                  (+)     (*)                  ____(=)____
                (A) (3) (5) (6)               (A)        (-)
                                                      (+)   (3)
                                                    (5) (6)
                En este caso siendo A=(5+6)-3
        Notese la forma en la que se resuelve

        @param arbol: Arbol que se va a desejar, se va a alterar
        @param letra: Letra que se va a despejar, ya que pueden que hayan varias
        @type arbol: Nodo()
        @type letra: str
        @return: Arbol ya despejado
        @rtype: Nodo()
        """
        if (self.letraEsta(arbol.der,letra)):
            #Esta en el lado derecho
            if (arbol.der.valor==letra):
                return arbol
            if (self.letraEsta(arbol.der.der),letra):
                #Lado derecho a la derecha
                arboltemp=None
                if (arbol.der.valor=="+" or arbol.der.valor=="*"):
                    arboltemp=self.convertir(arbol.der)
                    arboltemp=self.cruzar(arboltemp)
                    arbol.der=arbol.der.der
                    arboltemp.izq=arbol.izq
                if (arbol.der.valor=="-"):
                    #Derecho y menos al lado derecho
                    arboltemp=self.cruzar(arbol.der)
                    arboltemp.izq=arbol.izq
                    arbol.der=Nodo("*",Nodo("-1",None,None),arbol.der.der)
                if (arbol.der.valor=="/"):
                    #Derecho y div al lado derecho
                    arboltemp=self.convertir(arbol.der)
                    arboltemp.izq=arbol.izq
                    arbol.der=arbol.der.der
                arbol.izq=arboltemp
                return self.despejar(arbol,letra)
            else:
                #Lado derecho a la izquierda
                if (arbol.der.valor=="+" or arbol.der.valor=="*"):
                    #Der y mas al lado izq
                    arbol.der=self.cruzar(arbol.der)
                if (arbol.der.valor=="-" or arbol.der.valor=="/"):
                    #Der y menos al lado izq
                    arboltemp=self.convertir(arbol.der)
                    arboltemp.izq=arbol.izq
                    arbol.izq=arboltemp
                    arbol.der=arbol.der.izq
                return self.despejar(arbol,letra)
        else:
            #Esta del lado izquierdo
            if (arbol.izq.valor==letra):
                return arbol
            if (self.letraEsta(arbol.izq.izq,letra)):
                #En todos los casos se repite
                arboltemp=self.convertir(arboltemp)
                arboltemp.izq=arbol.der
                arbol.izq=arbol.izq.izq
                arbol.der=arboltemp
                return self.despejar(arbol,letra)
            else:
                #Lado Izquierdo a la derecha
                if (arbol.izq.valor=="+" or arbol.izq.valor=="*"):
                    #Izq y Suma al lado derecho
                    arbol.izq=self.cruzar(arbol.izq)
                if (arbol.izq.valor=="-"):
                    #Izq y Resta al lado derecho
                    arboltemp=self.cruzar(arbol.izq)
                    arboltemp.izq=arbol.der
                    arbol.izq(Nodo("*",Nodo("-1",None,None),arbol.izq.der))
                    arbol.izq=self.cruzar(arbol.izq)
                    arbol.der=arboltemp
                if (arbol.izq.valor=="/"):
                    #Izq y Div al lado derecho
                    arboltemp=self.convertir(arbol.izq)
                    arboltemp.izq=arbol.der
                    arbol.izq=arbol.izq.izq
                    arbol.der=arboltemp
                return self.despejar(arbol,letra)
