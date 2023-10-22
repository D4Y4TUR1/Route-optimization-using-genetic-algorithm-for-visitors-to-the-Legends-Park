import getdatos_1 as d
import random

import txt_1 as txt

lugares = d.getLugares_Completo()
matriz_adyacencia = d.getMatrizAdyacencia_Completa()

def lugares_interconectados(lugar):
    final = txt.leerDestino()
    
    # Obtener índice de "A" en la lista de lugares
    indice_lugar = lugares.index(lugar)
    
    # Acceder a la fila correspondiente en la matriz de adyacencia
    fila_conexiones = matriz_adyacencia[indice_lugar]
    
    # Encontrar los lugares conectados
    lugares_conectados = [lugares[i] for i, conexion in enumerate(fila_conexiones) if conexion == 1]
    
    # Imprimir los lugares conectados
    #print("Lugares conectados con :", lugares_conectados)
    
    # print("Antes: ", lugares_conectados)
    quedan = [elem for elem in lugares_conectados if elem != final]
    
    lugares_conectados = quedan
    
    return lugares_conectados
    

# r = lugares_interconectados('NC14')
# print(r)