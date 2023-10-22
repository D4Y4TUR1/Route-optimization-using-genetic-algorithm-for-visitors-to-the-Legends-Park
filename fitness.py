from collections import Counter

import getdatos_1 as d1
import getdatos_2 as d2

lugares = d1.getLugares_Completo()

distancias = d2.getMatrizDistancia_Completa()
tiempos = d2.getMatrizTiempo_Completa()
calificaciones = d2.getMatrizCalificacion_Completa()

def restar_repetidas(rutas):
    contador = Counter(rutas)
    restar1 = 0 
    restar2 = 0 

    
    elementos_repetidos = {elemento: contador[elemento] for elemento in contador if contador[elemento] > 1}
    
    # print(elementos_repetidos)
    
    for elemento, repeticiones in elementos_repetidos.items():
        # print(elemento)
        # print(repeticiones)
        if(repeticiones == 2):
            repeticiones = repeticiones*0.125#0.0625
            restar1 = restar1 + repeticiones
        else:
            repeticiones = repeticiones*0.25#0.3125
            restar2 = restar2 + repeticiones
        #print("El elemento '{}' se repite {} veces.".format(elemento, repeticiones))
    #print("restar: ", restar)

        
    restar = restar1+ restar2
    
    return restar

def fitness_3v(ruta):
    ru = ruta
    restar = restar_repetidas(ru)
    funcion = 0
    for i in range(len(ruta)-1):
        posicionX = lugares.index(ru[i])
        posicionY = lugares.index(ru[i+1])
        
        d = distancias[posicionX][posicionY]
        t = tiempos[posicionX][posicionY]
        c = calificaciones[posicionX][posicionY]
        #Ruta más
        #f = d*10 #Modicar retornar  = 1/funcion
        #Normal el variables
        # print("d: ", d)
        # print("t: ", t)
        # print("c: ", c)
        f = - d*0.1875 - t*0.1875 + c*0.25#- d*0.15625 - t*0.15625 + c*0.3125
        
        funcion = funcion + f
    #print("f: ", funcion)
    funcion = funcion - restar
    if(funcion<=0):
        funcion = funcion/(-100)

    return funcion
        

def calcular_aptitud(ruta):
    # Aquí puedes definir una función para calcular la aptitud de una ruta
    # basada en algún criterio de evaluación, por ejemplo, la distancia total.
    return 1/len(ruta)


# r = [['A', 'Z', 'O', 'NC12', 'P', 'K', 'NC13', 'NC14', 'NC16', 'NC17', 'V', 'W', 'NC18', 'U', 'NC19', 'T', 'NC3', 'NC4', 'NC5', 'NC6', 'NC7', 'NC8', 'H', 'G', 'NC9', 'D', 'NC10', 'C', 'B'], 
#['A', 'Z', 'O', 'Y', 'NC11', 'C', 'B']]

# r = ['A', 'Z', 'O', 'NC12', 'P', 'K', 'NC13', 'NC14', 'NC16', 'NC17', 'V', 'W', 'NC18', 'U', 'NC19', 'T', 'NC3', 'NC4', 'NC5', 'NC6', 'NC7', 'NC8', 'H', 'G', 'NC9', 'D', 'NC10', 'C', 'B']#['A', 'Z', 'O', 'Y', 'NC11', 'C', 'B']

# r =['Q', 'NC15', 'A', 'Z', 'O', 'NC12', 'P', 'NC12', 'NC8', 'H', 'G', 'H', 'G', 'H', 'G', 'H', 'NC8', 'NC11', 'B', 'C', 'H', 'G', 'H', 'NC8', 'NC12', 'P', 'K', 'T', 'K', 'T', 'NC3', 'L', 'S', 'NC2', 'NC1', 'R']
# f = fitness_3v(r)
# print(f)