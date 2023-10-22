import random
import getdatos_1 as d

import getrutasinicial_sr_1 as grisr1

import txt_1 as txt

lugares = d.getLugares_Completo()
matriz_adyacencia = d.getMatrizAdyacencia_Completa()


def ruta_totales(origen, destino, iteraciones):
        
    rutas_generadas = []
    
    for i in range(iteraciones):
        ruta = generar_ruta_interconectada_rr(origen, destino)
        
        rutas_generadas.append(ruta)
    
    rutas_generadas_sin_repetir = list(map(list, set(map(tuple, rutas_generadas))))
        
    return rutas_generadas_sin_repetir

def separar_rutas_x_cantidad(origen, destino):
    rutas = grisr1.generar_rutas_sr_v(origen, destino)
    
    #El elemento con mayor longitud
    elemento_mayor = max(rutas, key=len)
    maximo = len(elemento_mayor)
    #print("maximo: ", maximo)
    elemento_menor = min(rutas, key=len)
    minimo = len(elemento_menor)
    #print("minimo: ", minimo)
    t_maximo = maximo#+ 10
    
    ####
    rutas_formadas1 = ruta_totales(origen, destino, 3000)
    #rutas_formadas2 = ruta_totales(origen, destino, 500)
    rutas_formadas = []
    longitud = []
    for i in range(minimo, t_maximo+1):
        elementos_longitud_especifica = [sublista for sublista in rutas_formadas1 if len(sublista) == i]
        
        if(len(elementos_longitud_especifica)>0):
            longitud = longitud + [i]
            rutas_formadas = rutas_formadas + elementos_longitud_especifica
    return rutas_formadas, longitud

def generar_rutas_simples(origen, destino):
    archivo1 = "rutas_inicial_r_repetir.txt"
    archivo2 = "rutas_inicial_r_repetir-longitudes.txt"
    txt.eliminarMTXT(archivo1)
    txt.eliminarMTXT(archivo2)
    rutas, longitudes =separar_rutas_x_cantidad(origen, destino)
    txt.guardarMTXT(archivo1, rutas)
    txt.guardarMTXT(archivo2, longitudes)
    
    return rutas, longitudes



def generar_ruta_interconectada_rr(origen, destino):#, lugares, matriz_adyacencia):
    ruta = [origen]
    lugar_actual = origen
    
    # if(origen == destino):
    #     cp = [lugares[i] for i, conexion in enumerate(matriz_adyacencia[lugares.index(lugar_actual)]) if conexion == 1]
    #     #print("CP: ",cp)
    #     if cp:
    #         sl = random.choice(cp)
    #         lugar_actual = sl
    #         ruta.append(sl)
    
    while lugar_actual != destino:
        conexiones_posibles = [lugares[i] for i, conexion in enumerate(matriz_adyacencia[lugares.index(lugar_actual)]) if conexion == 1]
        
        if conexiones_posibles:
            siguiente_lugar = random.choice(conexiones_posibles)
            ruta.append(siguiente_lugar)
            lugar_actual = siguiente_lugar
        else:
            break
    
    return ruta


# origen='X'
# destino='Q'
# # #r = ruta_totales(origen, destino)
# r, l =separar_rutas_x_cantidad(origen, destino)
# print("R: ", r)
# print("L: ", len(r))
# print("Valores: ", l)
# p, l = generar_rutas_rr(origen, destino)
# print(p)
# print(l)