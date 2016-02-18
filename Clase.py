import math
import matplotlib.pylab as plt

class Onda:
    arreglo=[]
    def __init__(self,frecuencia,sampleo,bits,tiempo):
        self.FSampleo = sampleo
        self.NumeroBit = bits
        self.Segundos = tiempo
        self.Frecuencia = frecuencia
        self.Tamano =  sampleo * tiempo

    def generar(self):

        for i in range(0,self.Tamano):

            datos = (((2*(2**self.NumeroBit)/2)/math.pi)*math.atan(math.tan(1/math.pi*self.Frecuencia*i))/self.FSampleo)
            Onda.arreglo.append(datos)
            #print datos

        return Onda.arreglo

    def graficar(self,arreglo):
        plt.plot(arreglo, color="blue" , linewidth=1, linestyle="-")
        plt.show()