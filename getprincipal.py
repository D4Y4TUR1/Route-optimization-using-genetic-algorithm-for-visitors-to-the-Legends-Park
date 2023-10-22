import tkinter as tk
from tkinter import ttk

import getdatos_1 as ode1

import getgraficainicial as gi

import getgraficafinal as gf

import getgeneral as ge

lista_nodo = ode1.getLugares()
lista_nombre = ode1.getLugares_Nombres()


def recorrido(origen, destino, lbl_resultado1):
    
    posicionOrigen = lista_nombre.index(origen)
    print("Origen: ", posicionOrigen)
    posicionDestino = lista_nombre.index(destino)
    print("Destino: ", posicionDestino)
    resultado = int(posicionOrigen) + int(posicionDestino)
    lbl_resultado1.config(text="Resultado: " + str(resultado))
    
    print("Nodo Origen: ", lista_nodo[posicionOrigen])
    print("Nodo Final: ", lista_nodo[posicionDestino])
    print("Suma: ", lista_nodo[posicionOrigen]+lista_nodo[posicionDestino])
    
    a= ge.general(lista_nodo[posicionOrigen], lista_nodo[posicionDestino])
    #general.general(lista_nodo[posicionOrigen], lista_nodo[posicionDestino])
    
    # a= ['Q', 'NC15', 'A', 'NC14', 'NC13', 'K', 'P', 'NC12', 'O', 'Y', 'NC11',
    #     'B', 'C', 'NC10', 'D', 'NC9', 'G', 'H', 'NC8', 'NC7', 'NC6', 'NC5',
    #     'NC4', 'NC3', 'N', 'M', 'NC20', 'NC19', 'U', 'NC18', 'W', 'V', 'NC17',
    #     'X']
    gf.grafica_final(a)
    
def mostrarGraficaIncial():
    gi.grafica_inicial()
    print("Hola")
    

# Crear la ventana principal
ventana = tk.Tk()

# Configurar la ventana
ventana.title("Parque de las Leyendas")
ventana.geometry("1020x520")

# Crear los ComboBox
#combo1 = ttk.Combobox(ventana, values=lista_nombre)
#lbl_txt1 = tk.Label(ventana, text="Origen: ")
lbl_txt1 = tk.Label(ventana, text="Origen:", width=8, height=2, font=("Arial", 26))
lbl_txt1.place(x=3, y=3)
combo1 = ttk.Combobox(ventana, values=lista_nombre, width=30, height=8, font=("Arial", 26))
combo1.place(x=190, y=20)
#lbl_txt2 = tk.Label(ventana, text="Destino: ")
lbl_txt2 = tk.Label(ventana, text="Destino:", width=8, height=2, font=("Arial", 26))
lbl_txt2.place(x=3, y=80)
#combo2 = ttk.Combobox(ventana, values=lista_nombre)
combo2 = ttk.Combobox(ventana, values=lista_nombre, width=30, height=8, font=("Arial", 26))
combo2.place(x=190, y=97)

# Crear la etiqueta para mostrar el resultado
lbl_resultado = tk.Label(ventana, text="Resultado: ")
lbl_resultado.place(x=10, y=250)

# Crear el botón
#btn_sumar = tk.Button(ventana, text="Sumar", command=lambda: sumar(combo1.get(), combo2.get(), lbl_resultado))
btn_mapa = tk.Button(ventana, text="Mostrar Mapa", command= mostrarGraficaIncial, 
                      width=12, height=1, font=("Arial", 20),bg="gray", fg="black")
btn_mapa.place(x=28, y=180)

btn_sumar = tk.Button(ventana, text="Generar Recorrido", command=lambda: recorrido(combo1.get(), combo2.get(), lbl_resultado), 
                      width=15, height=1, font=("Arial", 20),bg="gray", fg="black")
btn_sumar.place(x=650, y=180)

# Ejecutar el bucle de eventos
ventana.mainloop()
