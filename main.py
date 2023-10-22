import getgraficainicial as gi

import getgraficafinal as gf

import getgeneral as ge


def menu(origen, destino):
    
    a= ge.general(origen, destino)
    mostrarGraficaIncial()
    mostrarGraficaFinal(a)


def mostrarGraficaIncial():
    gi.grafica_inicial()

def mostrarGraficaFinal(ruta):
    gf.grafica_final(ruta)
    
    
inicio = "Q"
fin = "R"

#QR 
#

menu(inicio, fin)