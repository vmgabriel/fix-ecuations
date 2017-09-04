# Integrantes del Grupo
    
* Carlos Andrés Aguirre Cañas
* Dalia Muñoz Araque
* Gabriel Vargas Monroy

# Arboles Binarios Aritmeticos en Python
    Este repositorio abarca ejercicios de aplicación de datos como Arboles binarios en el lenguaje de programación Python.

## Python:
 ![GitHub](/img/python-logo.png)
 
Using:
* [x] [Python](https://www.python.org/) 

# Arbol Aritmetico
![Logo](/img/arbolAritmetico.png)

## Código

```python
		
#Clase Nodo
class Nodo():
	def __init__(self,valor,izq=None,der=None):
		self.valor=valor
		self.izq=izq
		self.der=der

from nodo import Nodo.

#Clase evaluarExpresion para arboles aritmeticos.
class evaluarExpresion:
    def __init__(self):
        pass

    def evaluar(self, arbol):
        if arbol.valor=="+":
            return self.evaluar(arbol.izq)+self.evaluar(arbol.der)
        if arbol.valor=="-":
            return self.evaluar(arbol.izq)-self.evaluar(arbol.der)
        if arbol.valor=="*":
            return self.evaluar(arbol.izq)*self.evaluar(arbol.der)
        if arbol.valor=="/":
            return self.evaluar(arbol.izq)/self.evaluar(arbol.der)
        return int(arbol.valor)
```