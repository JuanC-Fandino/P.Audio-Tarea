from Clase import Onda
from archivar import Archivo
from Cuadrada import OndaC

def main():

    print ("Generador de Ondas \nV 1.0 \n")

    opcion = input("Ingrese el numero correspondien segun el tipo de Onda que desea generar:\n1.Sierra\n2.Cuadrada\n\n")

    if opcion==1:

        print ("Ingrese los parametros: ")
        Tono = input("Ingrese la frecuencia del tono a generar: ")
        Tiempo = input("Ingrese el tiempo de audio en segundos: ")
        Frecuenciadesampleo = input("Ingrese la frecuencia de muestreo: ")
        MaxBits = input("Ingrese el numero de bits: ")
        Nombre = raw_input("Ingrese el nombre del archivo a generar: ")
        Nombre = (Nombre + ".wav")



        sinusoidal = Onda (Tono, Frecuenciadesampleo, MaxBits, Tiempo)
        datos = sinusoidal.generar()

        archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
        archivo.archivar(datos)

        sinusoidal.graficar(datos)

    elif opcion==2:

        print ("Ingrese los parametros: ")
        Tono = input("Ingrese la frecuencia del tono a generar: ")
        Tiempo = input("Ingrese el tiempo de audio en segundos: ")
        Frecuenciadesampleo = input("Ingrese la frecuencia de muestreo: ")
        MaxBits = input("Ingrese el numero de bits: ")
        Nombre = raw_input("Ingrese el nombre del archivo a generar: ")
        Nombre = (Nombre + ".wav")
        print(Frecuenciadesampleo)


        square = OndaC (Tono, Frecuenciadesampleo, MaxBits, Tiempo)
        datos = square.generarC()

        archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
        archivo.archivar(datos)

        square.graficarC(datos)

    else:
        print("Opcion no valida")





if __name__ == "__main__":
    main()
