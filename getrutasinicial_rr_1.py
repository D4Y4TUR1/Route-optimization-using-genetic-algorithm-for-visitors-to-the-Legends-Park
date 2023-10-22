import random
import getdatos_1 as d

import getrutasinicial_sr_1 as grisr1

import txt_1 as txt

lugares = d.getLugares_Completo()
matriz_adyacencia = d.getMatrizAdyacencia_Completa()


def generar_rutas_rr(origen, destino):
    archivo1 = "rutas_inicial_r_repetir.txt"
    archivo2 = "rutas_inicial_r_repetir-longitudes.txt"
    txt.eliminarMTXT(archivo1)
    txt.eliminarMTXT(archivo2)
    rutas, longitudes = ruta_formada_rr(origen, destino)
    txt.guardarMTXT(archivo1, rutas)
    txt.guardarMTXT(archivo2, longitudes)
    
    return rutas, longitudes
       
def ruta_x_cantidad(origen, destino, cantidad):
    
    verificarVacio = True
    contar = 0
    
    while(verificarVacio):
        
        rutas_generadas = []
        
        for i in range(50):
            ruta = generar_ruta_interconectada_rr(origen, destino)
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
            if(contar >20):
                #print("SE termino")
                return []

def ruta_formada_rr(origen, destino):
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
    rutas_formadas = []
    longitud = []
    for i in range(minimo, t_maximo+1):
        r = ruta_x_cantidad(origen, destino, i)
        rutas_formadas = rutas_formadas + r
        if(len(r)>0):
            longitud = longitud + [i]
    return rutas_formadas, longitud

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
# p, l = generar_rutas_rr(origen, destino)
# print(p)
# print(l)