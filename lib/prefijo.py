# -*- coding: utf-8 -*-

# Ejercicio de construcción de arboles en PREORDEN.

import pila
from nodo import Nodo

class preFijo(object):
	def __init__(self):
		pass

	def construirPre(self,lista):
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