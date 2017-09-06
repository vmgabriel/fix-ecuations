#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Archivo para cli

@author: Andres Aguirre - Dalia Muñoz - Gabriel Vargas
@version: 0.1
@license: GPL
@contact: vmgabriel96@gmail.com
"""

import sys
sys.path.append("../lib/")
#Para librerias que se encuentren en el directorio padre

from lib.pila import Pila
from lib.nodo import Nodo
from lib.posfijo import posFijo
from lib.prefijo import preFijo
#from evaluar import evaluarExpresion

class Cli(object):
    """
    Clase B{Cli} enfocada en que cargue todos los avisos del terminal
    """

    def __init__(self):
        """Inicializador(constructor) de la clase I{Cli}"""
        self.seguir = True
        """Funciona como una variable Bandera"""
        self.arboles=[]
        """Variable que guardara un arreglo de Nodos"""

    def separador(self):
        """Metodo centrado en separar en consola"""
        print ("------------------")

    def bienvenida(self):
        """Metodo centrado en darle bienvenida al usuario, usa I{separador()}"""
        self.separador()
        print ("Bienvenido a Arbol Algoritmico")
        self.separador()

    def menu(self):
        """
        Metodo del menu principal, enfocado en mostrar un menu para quedar
        el usuario seleccione con la entrada, en este caso el menu muestra las
        siguientes opciones:

            1. Ingresar Ecuaciones: Enfocado en resolver ecuaciones I{X} por I{X}
            2. Evaluar arbol: Enfocado en resolver un arbol previamente guardado
            3. Salir: Da fin al programa.

        @return: valor numero de seleccion del usuario
        @rtype: int
        """
        self.separador()
        print ("1. Ingresar Ecuaciones")
        print ("2. Evaluar el arbol")
        print ("3. Salir")
        print("Que desea hacer?:")
        return int(input())

    def posicion(self):
        """
        Metodo para seleccion del usuario del tipo del orden de la ecuacion
        los posibles casos son:

            1. Pre-orden
            2. Pos-orden

        @return: valor numero de seleccion del usuario
        @rtype: int
        """
        self.separador()
        print ("1. Pre-Orden")
        print ("2. Pos-Orden")
        print ("Cual desea escojer?:")
        return int(input())


    def construirPila(self):
        """
        Metodo para construir Pila, siendo pila un esquema LIFO

        .....* 1 * <-- Apilar  // ---> Desapilar el primero
        .....* 2 *
        .....* 3 *
        .....* 4 *
        .....* 5 *
        .....*****

        @return: Pila de datos insertados por el usuario está en B{lib/pila.py}
        @rtype: Pila()
        """
        pila = Pila()
        self.separador()
        seguirtemp= True
        """Variable temporal estilo bandera para el while"""
        while (seguirtemp):
            print ("Ingrese el valor a apilar: ")
            pila.apilar(input())
            print ("Desea seguir agregando a la pila(1. Si, 2. No): ")
            if (int(input()) == 2):
                seguirtemp=False
        """@note: Se apila minimo 1, se permite al usuario escojer la cantidad que
            desea ingresar siendo 1. si y 2. no"""
        return pila

    def construirArreglo(self):
        """
        Metodo para construir en base a un arreglo, teniendo los datos que el
        usuario desee.

        .........[ A B C D ] <---Agregar

        @return: Un arreglo de tipo str
        @rtype: str[]
        """
        arreglo = []
        self.separador()
        seguirtemp= True
        """@var seguirtemp: Variable temporal estilo bandera para el while"""
        while (seguirtemp):
            print ("Ingrese el valor a agregar: ")
            arreglo.append(input())
            print ("Desea seguir agregando(1. Si, 2. No): ")
            if (int(input()) == 2):
                seguirtemp=False
        """@note: Se apila minimo 1, se permite al usuario escojer la cantidad que
            desea ingresar siendo 1. si y 2. no"""
        return arreglo

    def salida(self):
        """Metodo centrado en darle fin al usuario, usa I{separador()}, si llega aqui su salida
            es satisfactoria"""
        self.separador()
        print ("Gracias por usar el servicio")
        self.separador()

    def imprimirResultado(self, arbol):
        """
        Metodo enfocado en imprimir Resultado de la solucion del arbol, vease la documentacion

        ...........(+)          (4+3)   +   (7-5)
        .......(+)     (-)        7     +     2
        .....(4) (3) (7) (5)            9  <--------Imprime este resultado

        @param arbol: arbol que se va a resolver
        @type arbol: Nodo()
        """
        self.separador()
        resultado = evaluarExpresion()
        print ("El resultado del arbol es: "+ str(resultado.evaluar(arbol)))
        self.separador()

    def run(self):
        """
        Metodo principal, correra el ciclo principal al usuario y adherida todas las funciones del Cli()
        """
        while (self.seguir):
             x = self.menu()
             if (x == 1):
                 print ("Ingrese la cantidad de ecuaciones: ")
                 cant=int(input())
                 for y in range(0,cant):
                     self.separador()
                     print ("Ecuacion "+str(y+1))
                     self.separador()
                     arreglotemp=self.construirArreglo()
                     if (self.posicion()==1):
                         pre=preFijo()
                         self.arboles.append(pre.construirPre(arreglotemp))
                     else:
                         pos=posFijo()
                         self.arboles.append(pos.convertirPos(arreglotemp))
                     print ("Hecho Correctamente")
             elif (x == 2):
                 if not(self.arboles == []):
                     self.imprimirResultado(self.arboles[0])
             else:
                self.seguir = False
        self.salida()
