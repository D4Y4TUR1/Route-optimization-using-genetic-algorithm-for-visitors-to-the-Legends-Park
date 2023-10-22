# Lista de lugares
import getdatos_1 as d

import txt_1 as txt

lugares = d.getLugares_Completo()

# Matriz de adyacencia que representa las conexiones entre los lugares
matriz_adyacencia = d.getMatrizAdyacencia_Completa()

def generar_rutas_sr(origen, destino):
    archivo = "rutas_inicial_sin_repetir.txt"
    
    txt.eliminarMTXT(archivo)
    rutas = generar_rutas(origen, destino)
    txt.guardarMTXT(archivo, rutas)
    
    return rutas

def generar_rutas_sr_v(origen, destino):
    # archivo = "rutas_inicial_sin_repetir.txt"
    
    # txt.eliminarMTXT(archivo)
    rutas = generar_rutas(origen, destino)
    # txt.guardarMTXT(archivo, rutas)
    
    return rutas



def generar_rutas(origen, destino):
    rutas = []
    ruta_actual = [origen]

    def buscar_rutas(lugar_actual):
        if lugar_actual == destino:
            rutas.append(ruta_actual.copy())
            return

        for i, conexion in enumerate(matriz_adyacencia[lugares.index(lugar_actual)]):
            if conexion == 1 and lugares[i] not in ruta_actual:
                ruta_actual.append(lugares[i])
                buscar_rutas(lugares[i])
                ruta_actual.pop()

    buscar_rutas(origen)
    
    return rutas

# Ejemplo de uso
# origen = "X"
# destino = "Q"

# rutas = generar_rutas_sr(origen, destino)
# #print("Rutas: ", rutas)
# print("Cantidad: ", len(rutas))
# elemento_mayor = max(rutas, key=len)
# print("Mayor: ", elemento_mayor)
# print("Long M: ",len(elemento_mayor))

# elemento_menor = min(rutas, key=len)
# print("Menor: ", elemento_menor)
# print("Long N: ",len(elemento_menor))

# rr = txt.leerMTXT("rutas_inicial_sin_repetir.txt")
# print("RR: ", len(rr))

# print(f"Todas las rutas desde {origen} hasta {destino}:")
# for ruta in rutas:
#     print(ruta)
