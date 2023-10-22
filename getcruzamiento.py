import random

import getpadre1segmento_1 as gp1s

import getpadre2segmento_1 as gp2s

import getrutasintermedia_igual_1 as grii1

import getnodosadyascente_1 as gna1

import getrutasintermedia_rr_1 as rr1
import getrutasintermedia_sr_1 as sr1

def juntar(origen, destino, cantidad):
    
    rr = rr1.rutas_intermedias_x_cantidad_rr_quitando_final(origen, destino, cantidad)
    sr = sr1.rutas_intermedias_x_cantidad_sr_quitando_final(origen, destino, cantidad)
    
    total = sr + rr
    total_sin_repetir = list(map(list, set(map(tuple, total))))
    
    return total_sin_repetir

def cruzar(padre1, padre2):
    hijo = [None] * len(padre1)
    #Copiar los elementos del padre1 al hijo
    hijo, guardar,origen,destino,ini,fin,cantidad = gp1s.padre1_segmento(padre1)
    inicio = ini - 1
    final = fin + 1
    
    # print("Hijo Inicio: ", hijo)
    
    # Completar el hijo con los elementos del padre2 que no están en el padre1
    segmento2 = gp2s.segmentos(padre2, origen, destino, cantidad)
    #print(segmento2)
    if(len(segmento2) == 0):
        # print("Falta")
        if(origen == destino):
            if(cantidad == 3):
                lugar = gna1.lugares_interconectados(origen)
                hijo[inicio+1] = random.choice(lugar)
                # print("Hijo p1: ", hijo)
            else:
                if(cantidad >3):
                    rutas_igual = grii1.rutas_intermedias_x_cantidad_igual_quitando_final(origen, destino, cantidad)
                    if(len(rutas_igual) > 0):
                        segmento_aleatorio = random.choice(rutas_igual)
                        for i in range(len(segmento_aleatorio)):
                            hijo[inicio+i] = segmento_aleatorio[i]
                            # print("Hijo p2: ", hijo)
                    else:
                        hijo[ini:fin+1] = guardar[ini:fin+1]
                else:
                    print("Está mal el cruzamiento1")
        else:
            ruta_total = juntar(origen, destino, cantidad)
            if(len(ruta_total) != 0):
                segmento_aleatorio = random.choice(ruta_total)
                for i in range(len(segmento_aleatorio)):
                    hijo[inicio+i] = segmento_aleatorio[i]
                # print("Hijo p3: ", hijo)
            else:
                # print("Aqui es")

                hijo[ini:fin+1] = guardar[ini:fin+1]
            
    else:
        segmento_aleatorio = random.choice(segmento2)
        for i in range(len(segmento_aleatorio)):
            hijo[inicio+i] = segmento_aleatorio[i]
        # print("Hijo p4: ", hijo)
    
    # print("Hijo Final: ", hijo)
    return hijo
            
def cruzamiento(padres):
    m= padres 
    m = cruzamiento_pmx(m)
    poblacion = m
    
    return poblacion
    
    
def cruzamiento_pmx(padres):
    hijos=[]
    padresT =  padres.copy()
    if(len(padres) % 2 != 0):
        # indice = random.randint(0, len(padresT) - 1)
        # padresT.append(padres[indice])
        indice = random.randint(0, len(padresT) - 1)
        hijos.append(padresT[indice])
        padresT.remove(padresT[indice])
    
    contadorH = 0
    # print("")
    # print("Cantidad: ", len(padresT)/2)
    contador = int(len(padresT)/2)
    while contadorH < contador:
        indice1 = random.randint(0, len(padresT) - 1)
        indice2 = random.randint(0, len(padresT) - 1)
        padre1 = padresT[indice1]
        padre2 = padresT[indice2]
        #//print("Padre1: ", padre1)
        #//print("Padre2; ", padre2)
        if(indice1 != indice2):
            hijo1 = cruzar(padre1, padre2)
            hijo2 = cruzar(padre2, padre1)#cruzar(padre1, padre2)
            hijos.append(hijo1)
            hijos.append(hijo2)
            padresT.remove(padre1)
            padresT.remove(padre2)
            # print("Indice 1: ", indice1)
            # print("Indice 2: ", indice2)
            contadorH = contadorH + 1
    
    # print("")
    # print("PADREST: ", padresT)
    # print("")
    # print("")
    # print("contadorH: ", contadorH)
    return hijos


    

# padres = [['C', 'H', 'C', 'NC10', 'G', 'NC9', 'E'], ['C', 'NC10', 'G', 'NC10', 'D', 'NC9', 'E']]#[1,2,3,4,5,6,7]#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # padre2 = ['A','B', 'C', 'D', 'E']#[['A','B', 'C', 'D', 'E'], [['A','B', 'C', 'D', 'E']]]#[1,2,3,4,5,6,7,10,11,12,1,2,3,8,5,6,7]
# # #gp1s.padre1_segmento(padre1)
# # #cruzar(padre1,padre2)
# print("CRUZ: ", cruzamiento(padres))