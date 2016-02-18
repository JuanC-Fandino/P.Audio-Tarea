import math
import matplotlib.pylab as plt

class OndaC:
    array=[]
    def __init__(self,frecuencia,sampleo,bits,tiempo):
        self.FSampleo = sampleo
        self.NumeroBit = bits
        self.Segundos = tiempo
        self.Frecuencia = frecuencia
        self.Tamano =  sampleo * tiempo

    def generarC(self):

        for i in range(1,self.Tamano):

            datos = (((2**self.NumeroBit)/2) * (1/math.sin(2*math.pi*self.Frecuencia*i))*math.fabs(math.sin(2*math.pi*self.Frecuencia*i)))/self.FSampleo
            OndaC.array.append(datos)


        return OndaC.array

    def graficarC(self,array):
        plt.plot(array, color="green" , linewidth=1, linestyle="-")
        plt.show()