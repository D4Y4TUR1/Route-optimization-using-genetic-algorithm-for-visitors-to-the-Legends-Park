import random
import getdatos_1 as d

import txt_1 as txt

lugares = d.getLugares_Completo()
matriz_adyacencia = d.getMatrizAdyacencia_Completa()

def rutas_intermedias_x_cantidad_igual_quitando_final(origen, destino, cantidad):
    final = txt.leerDestino()
    
    rutas = ruta_x_cantidad(origen, destino, cantidad)
    
    quedan = [elem for elem in rutas if elem.count(final) <= 0]
    
    
    # Filtrar los elementos de la misma longitud
    elementos_misma_longitud = [elem for elem in quedan if len(elem) == cantidad]
    
    rutas = elementos_misma_longitud
    
    return rutas

def ruta_x_cantidad(origen, destino, cantidad):
    
    verificarVacio = True
    contar = 0
    
    while(verificarVacio):
        
        rutas_generadas = []
        
        for i in range(50):
            ruta = generar_ruta_interconectada_igual(origen, destino)
            if(len(ruta) == cantidad):
                rutas_generadas.append(ruta)
        
        rutas_generadas_sin_repetir = list(map(list, set(map(tuple, rutas_generadas))))
        
        if(len(rutas_generadas_sin_repetir)>0):
            
            verificarVacio=False
            #print("SE GUARDO")
            return rutas_generadas_sin_repetir
        else:
            #print("Rutas generadas:", rutas_generadas)
            contar = contar +1
            if(contar >10):
                #print("SE termino")
                return []


def generar_ruta_interconectada_igual(origen, destino):#, lugares, matriz_adyacencia):
    ruta = [origen]
    lugar_actual = origen
    
    if(origen == destino):
        cp = [lugares[i] for i, conexion in enumerate(matriz_adyacencia[lugares.index(lugar_actual)]) if conexion == 1]
        #print("CP: ",cp)
        if cp:
            sl = random.choice(cp)
            lugar_actual = sl
            ruta.append(sl)
    
    while lugar_actual != destino:
        conexiones_posibles = [lugares[i] for i, conexion in enumerate(matriz_adyacencia[lugares.index(lugar_actual)]) if conexion == 1]
        
        if conexiones_posibles:
            siguiente_lugar = random.choice(conexiones_posibles)
            ruta.append(siguiente_lugar)
            lugar_actual = siguiente_lugar
        else:
            break
    
    return ruta


# origen='C'
# destino='E'
# #p = generar_ruta_interconectada_igual(origen, destino)
# p = rutas_intermedias_x_cantidad_igual_quitando_final(origen, destino, 7)
# print(p)