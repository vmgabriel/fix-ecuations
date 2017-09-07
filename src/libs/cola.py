#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Libreria basica COLA

@author: Andres Aguirre - Dalia Muñoz - Gabriel Vargas
@version: 0.1
@license: GPL
@contact: vmgabriel96@gmail.com
"""

class Cola(object):
    """ Representa una cola con operaciones de encolar, desencolar y
        verificar si está vacia. """

    def __init__(self):
        """Crea una cola vacia. """
        # La cola vacía se representa con una lista vacía
        self.items=[]

    def encolar(self, x):
        """
        Agrega el elemento x a la cola.

        @param x: Elemento a encolar
        """
        # Encolar es agregar al final de la cola.
        self.items.append(x)

    def desencolar(self):
        """ Devuelve el elemento inicial y lo elimina de la cola.
        Si la cola está vacía levanta una excepción.

        @return: Dato desencolado, el inicial
        """
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola está vacía")

    def es_vacia(self):
        """
        Devuelve True si la lista está vacía, False si no.

        @return: True si está vacio
        @rtype: bool
        """
        return self.items == []

    def cantidad(self):
        """
        Returna la cantidad de datos en la cola.

        @return: Cantidad de datos en la cola
        @rtype: int
        """
        return len(self.items)                                                                                                                                        
