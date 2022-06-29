import random

from numpy import *

class Generadorlista:

    def generarListaUsuario(self):
        Lista=[]
        self.x=int(input("ingrese la cantidad de valores: "))
        for x in range (self.x):
            a=int(input('"De una numero entero: '))
            Lista.append(a)
        print(Lista)

    def GenerarListaAleatorio(self):
        Lista=[]
        I=int(input("Inserte Limite Inicial: "))
        F=int(input("Inserte Limite Final: "))
        for x in range(self.x):
            a=random.randint(I,F)
            Lista.append(a)
        print(Lista)
        

Migenerador=Generadorlista()
Migenerador.generarListaUsuario()
Migenerador.GenerarListaAleatorio()
""""
    def generarListaAleatoria(self,n,x,y):
        lista=[]

        for _ in range[0,n]:
            lista.append(random.randint(x,y))
        print (lista)
        return lista

Migenerador=Generadorlista()
Migenerador.generarListaAleatoria()

class Multiplicadorlistas (Generadorlista):
    a=np.array([])
    b=np.array([])
    mu=a*b 
    print (mu)

Multiplicadorlistas.generarListaAleatoria
