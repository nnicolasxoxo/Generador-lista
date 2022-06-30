from Archivo1 import Generadorlista
class multiplicadorListas(Generadorlista):

    def multiplicarListas(self, a, b):
        lista_multiplicador= [a[i]* b[i] for i in range (len(b))]
        print ("a*b =  ", lista_multiplicador)
        return lista_multiplicador
        

