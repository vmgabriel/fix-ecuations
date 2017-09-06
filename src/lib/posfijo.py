#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.nodo import Nodo
from lib.pila import Pila

#convertira de posfijo a arbol

class posFijo(object):
	def __init__(self):
		pass

	def convertirPos(self,expresion):
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
