#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib/")
#Para librerias que se encuentren en el directorio padre

from lib.pila import Pila
from lib.nodo import Nodo
from lib.posfijo import posFijo
from lib.prefijo import preFijo
from lib.evaluar import evaluarExpresion

class Cli(object):

    def __init__(self):
        self.seguir = True
        self.arboles=[]

    def separador(self):
        print ("------------------")

    def bienvenida(self):
        self.separador()
        print ("Bienvenido a Arbol Algoritmico")
        self.separador()

    def menu(self):
        self.separador()
        print ("1. Ingresar Ecuaciones")
        print ("2. Evaluar el arbol")
        print ("3. Salir")
        print("Que desea hacer?:")
        return int(input())

    def posicion(self):
        self.separador()
        print ("1. Pre-Orden")
        print ("2. Pos-Orden")
        print ("Cual desea escojer?:")
        return int(input())


    def construirPila(self):
        pila = Pila()
        self.separador()
        seguirtemp= True
        while (seguirtemp):
            print ("Ingrese el valor a apilar: ")
            pila.apilar(input())
            print ("Desea seguir agregando a la pila(1. Si, 2. No): ")
            if (int(input()) == 2):
                seguirtemp=False
        return pila

    def construirArreglo(self):
        arreglo = []
        self.separador()
        seguirtemp= True
        while (seguirtemp):
            print ("Ingrese el valor a agregar: ")
            arreglo.append(input())
            print ("Desea seguir agregando(1. Si, 2. No): ")
            if (int(input()) == 2):
                seguirtemp=False
        return arreglo

    def salida(self):
        self.separador()
        print ("Gracias por usar el servicio")
        self.separador()

    def imprimirResultado(self, arbol):
     self.separador()
     resultado = evaluarExpresion()
     print ("El resultado del arbol es: "+ str(resultado.evaluar(arbol)))
     self.separador()

    def run(self):
        while (self.seguir):
             x = self.menu()
             if (x == 1):
                 print ("Ingrese la cantidad de ecuaciones: ")
                 cant=int(input())
                 for y in range(1,cant):
                     self.separador()
                     print ("Ecuacion "+str(y))
                     self.separador()
                     arreglotemp=self.construirArreglo()
                     if (self.posicion()==1):
                         pre=preFijo()
                         arboles.append(pre.construirPre(arreglotemp))
                     else:
                         pos=posFijo()
                         arboles.append(pos.convertirPos(arreglotemp))
                     print ("Hecho Correctamente")
             elif (x == 2):
                 if not(self.arbol == None):
                     self.imprimirResultado(self.arbol)
             else:
                self.seguir = False
        self.salida()
