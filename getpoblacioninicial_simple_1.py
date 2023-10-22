import random

# import rutas_todas_2 as rt2

# import ruta_forma_inicial as rfi

# import guardar_arrayb_txt_4 as ga

import getrutasinicial_sr_1 as grisr1
import getrutasinicial_simple_1 as grisimple1


import txt_1 as txt

def getpoblacion_inicial(num_individuos, origen, destino):
    txt.guardarDestino(destino)
    
    total_poblacion, longitud = juntar_rutas_solo(origen, destino)#juntar_rutas_tipos(origen, destino)
    poblacion_ini = getpoblacion(num_individuos, longitud, total_poblacion)
    
    return poblacion_ini

def juntar_rutas_solo(origen, destino):
    sr = grisr1.generar_rutas_sr(origen, destino)
    rr, long = grisimple1.separar_rutas_x_cantidad(origen, destino)#grirr1.generar_rutas_rr(origen, destino)
    
    total = rr
    total_sin_repetir = list(map(list, set(map(tuple, total))))
    
    return total_sin_repetir, long

def juntar_rutas_tipos(origen, destino):
    sr = grisr1.generar_rutas_sr(origen, destino)
    rr, long = grisimple1.separar_rutas_x_cantidad(origen, destino)#grirr1.generar_rutas_rr(origen, destino)
    
    total = sr + rr
    total_sin_repetir = list(map(list, set(map(tuple, total))))
    
    return total_sin_repetir, long


def getposiciones(num_individuos, long, total_pob):
    
    cant_indi = 0
    pos = []
    while (cant_indi < num_individuos):
        #print("Cant sin mod: ", cant_indi)
        #Array de la long minima al maximo
        array = long
        
        cantidad_el = int(len(array)*0.25)

        if(cantidad_el == 0):
            if(cant_indi < num_individuos):
                elementos_seleccionados = random.sample(array, num_individuos-cant_indi)
                cant_indi = cant_indi + num_individuos-cant_indi
                #print("Cant mod 1: ", cant_indi)
                pos = pos + elementos_seleccionados
        else:
            # Seleccionar aleatoriamente una cantidad de elementos del array
            if(num_individuos-cant_indi-1<cantidad_el):
                elementos_seleccionados = random.sample(array, num_individuos-cant_indi)
                cant_indi = cant_indi + num_individuos-cant_indi
                #print("Cant mod 2: ", cant_indi)
                pos = pos + elementos_seleccionados
            else:
                
                elementos_seleccionados = random.sample(array, cantidad_el)
                cant_indi = cant_indi + cantidad_el
                #print("Cant smod 3: ", cant_indi)
                pos = pos + elementos_seleccionados
        
        #print("Cant modifificada: ", cant_indi)
    return pos

def getpoblacion(num_individuos, long, total_pob):
    poblacion = total_pob
    if(len(poblacion)< num_individuos):
        return total_pob
    
    pob_n = []
    
    
    pos = getposiciones(num_individuos, long, total_pob)
    
    #print("POS: ",pos)
    
    cant = 0
    
    while(cant < len(pos)):
        pob_n_elementos_misma_longitud = [elem for elem in poblacion if len(elem) == pos[cant]]
        # Mostrar aleatoriamente dos elementos de la matriz
        #print(len(pob_n_elementos_misma_longitud))
        if(len(pob_n_elementos_misma_longitud)!= 0):
            elementos_mostrados = random.sample(pob_n_elementos_misma_longitud, 1)
            #print("EL: ",pob_n_elementos_misma_longitud)
            #print("TTT: ",elementos_mostrados)
            pob_n = pob_n + elementos_mostrados
            cant = cant+1
        else:
            cant = cant+1
            
    return pob_n
    

# p, l = juntar_rutas_solo('Q', 'R')
# print("p:", p)
# print("Long", len(p))
# print("l: ",l)

# Long 66
# l:  [17, 23, 27, 29, 30, 33]

# Long 7
# l:  [21, 23, 25, 30, 31, 33, 35]

# rutas = 46 + 20
# num_individuos = 20
# origen = "Q"#"X"
# destino = "R"

# # #rutas = crear_poblacion_inicial(origen, destino)
# rutas = getpoblacion_inicial(num_individuos, origen, destino)
# print("RR: ", rutas)
# print("Cantidad: ", len(rutas))





# elemento_mayor = max(rutas, key=len)
# print("Mayor: ", elemento_mayor)
# print("Long M: ",len(elemento_mayor))

# elemento_menor = min(rutas, key=len)
# print("Menor: ", elemento_menor)
# print("Long N: ",len(elemento_menor))

# print(f"Todas las rutas desde {origen} hasta {destino}:")
# for ruta in rutas:
#     print(ruta)getpoblacion