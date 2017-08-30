# -*- coding: utf-8 -*-
class Cola(object):
    """ Representa una cola con operaciones de encolar, desencolar y
        verificar si está vacía. """

    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa con una lista vacía
        self.items=[]

    def encolar(self, x):
        """ Agrega el elemento x a la cola. """
        # Encolar es agregar al final de la cola.
        self.items.append(x)

    def desencolar(self):
        """ Devuelve el elemento inicial y lo elimina de la cola.
        Si la cola está vacía levanta una excepción. """
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []

    def cantidad(self):
        """ Returna la cantidad de datos en la cola. """
        return len(self.items)
                                                                                                                                                    
