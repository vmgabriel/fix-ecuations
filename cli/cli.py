#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../lib/")
#Para librerias que se encuentren en el directorio padre

from pila import Pila
from nodo import Nodo
from posfijo import posFijo
from prefijo import preFijo
from evaluar import evaluarExpresion

class Cli(object):
	def __init__(self):
		self.seguir = True
		self.arbol=None

	def separador(self):
		print ("------------------")

	def bienvenida(self):
		self.separador()
		print ("Bienvenido a Arbol Algoritmico")
		self.separador()
		
	def menu(self):
		self.separador()
		print ("1. Ingreso en Pre-Orden")
		print ("2. Ingreso en Pos-Orden")
		print ("3. Evaluar el arbol")
		print ("4. Salir")
		print("Que desea hacer?:")
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
				prefijo=preFijo()
				self.arbol=prefijo.construirPre(self.construirArreglo())
				print ("Hecho correctamente!!")
			elif (x == 2):
				posfijo=posFijo()
				self.arbol=posfijo.convertirPos(self.construirArreglo())
				print ("Hecho correctamente!!")
			elif (x == 3):
					if not(self.arbol == None):
						self.imprimirResultado(self.arbol)
			else:
				self.seguir = False
		self.salida()

if __name__ == "__main__":
    run=Cli()
    run.run()
