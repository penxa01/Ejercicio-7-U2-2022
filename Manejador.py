import os
import csv 
from ViajeroFrecuente import ViajeroFrecuente


class Manejador:
    __ListaViajeros = []

    def __init__(self):
        self.__ListaViajeros = []

    def GenerarLista(self):
        rutaAbsoluta = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
        Archivo = os.path.join(rutaAbsoluta, "Viajeros.csv")
        archivo =open(Archivo)
        reader = csv.reader(archivo,delimiter=';')
        cabecera = True
        for comp in reader:
            if cabecera:
                cabecera= not cabecera
            else:
                NuevoViajero = ViajeroFrecuente(int(comp[0]),comp[1],comp[2],comp[3],int(comp[4]))
                self.__ListaViajeros.append(NuevoViajero)
        archivo.close

    def Listar(self):
        for i, viaj in enumerate(self.__ListaViajeros):
            print(viaj)
            print("".center(20,"-"))
    
    def Buscar(self,NroViaj):
        i = 0

        while((self.__ListaViajeros[i].GetNumViaj() != NroViaj) and (i< len(self.__ListaViajeros))):
            i += 1
        ViajeroEncontrado= self.__ListaViajeros[i]
        if(ViajeroEncontrado.GetNumViaj() == NroViaj):
            print("VIAJERO ENCONTRADO")
            print(ViajeroEncontrado)
        else:
            print("VIAJERO INEXISTENTE")
        return ViajeroEncontrado
        
    def MillasMaximas(self):
        viajeroMaximo = self.__ListaViajeros[0]
        for viajero in self.__ListaViajeros:
            if viajeroMaximo < viajero:
                viajeroMaximo = viajero
        return viajeroMaximo
    
    def CompararViajeros(self,Millas):
        print("Viajeros con millas acumuladas IGUAL al valor ingresado")
        for i in range(len(self.__ListaViajeros)):
            if (self.__ListaViajeros[i] == Millas):
                print("".center(20,"-"))
                print(self.__ListaViajeros[i])
                print("".center(20,"-"))

        

