import random
class Generadorlista:
    def generarListaUsuario(self):
        Lista=[]
        self.x=int(input("ingrese la cantidad de valores: "))
        for x in range (self.x):
            a=int(input('"De una numero entero: '))
            Lista.append(a)
        print(Lista)
        return Lista
    def GenerarListaAleatorio(self):
        Lista=[]
        I=int(input("Inserte Limite Inicial: "))
        F=int(input("Inserte Limite Final: "))
        for x in range(self.x):
            a=random.randint(I,F)
            Lista.append(a)
        print(Lista)
        return Lista

