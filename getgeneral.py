#import getpoblacioninicial as gpi
import getpoblacioninicial_simple_1 as gpisimple1

import getevolucionar as ge

import fitness as f



def algoritmo_genetico(num_individuos, origen, destino, tasa_mutacion, num_generaciones):
    
    mejor_costo = -float('inf')  # Mejor costo inicialmente infinito
    #print("INFINITO: ", 9>mejor_costo)
    # Inicializamos la población llamando a la función definida anteriormente
    #poblacionG = gpi.getpoblacion_inicial(num_individuos, origen, destino)#pir1.poblacion_inicial(num_individuos, origen, destino)
    poblacionG = gpisimple1.getpoblacion_inicial(num_individuos, origen, destino)
    
    
    #poblacionG = p.crear_poblacion_inicial(num_individuos, origen, destino)#inicializar_poblacion(tareas, trabajadores, num_individuos)
    print("POBLACION INICIAL")
    print("------------------")
    print("cantidad: ",len(poblacionG))
    print(poblacionG)
    print("------------------")
    #return poblacionG, 0, 0, 0,0
    
    #---------------------------------------------#
    generacion = 0
    iteracionMejor = 0
    for x in range(num_generaciones):
        if(x!=0):
            # Evolucionar población
            poblacionG = ge.evolucionar_poblacion(poblacionG, num_individuos, tasa_mutacion, x)#ev.evolucionar_poblacion(poblacionG, num_individuos, tasa_mutacion, x)
    
    #     # Evaluar población
        evaluaciones = [f.fitness_3v(ruta) for ruta in poblacionG]#[f.calcular_aptitud(ruta) for ruta in poblacionG]
        
        
        
        #print("EEE: ", evaluaciones)
        # Obtener mejor individuo y su costo
        mejor_individuo = poblacionG[evaluaciones.index(max(evaluaciones))]
        
        ################################################################
        #print("NNN: ", evaluaciones.index(max(evaluaciones)))
        print("")
        print("#####################################")
        print("Generacion ", x)
        print("Mejor individuo: ", mejor_individuo)
        cruta_actual = max(evaluaciones)
        print("Mayor fitness: ", cruta_actual)
        print("#####################################")
        ####################################################################
        
        # Actualizar mejor costo y criterio de parada
        if cruta_actual > mejor_costo:
            mejor_costo = cruta_actual
            mejor_individuo1 = mejor_individuo
            iteracionMejor = x
            generacion = 0
        else:
            generacion = generacion + 1
            # Si el costo no mejora en varias generaciones, se alcanza el criterio de parada
            if generacion >= 20:  # Puedes ajustar este valor según tus necesidades
                print("APAGAR")
                return poblacionG, mejor_individuo1, mejor_costo, x, iteracionMejor
    
    #---------------------------------------------#
    
    
    
    
    return poblacionG, mejor_individuo1, mejor_costo, x, iteracionMejor

def general(origen, destino):
    
    # Parámetros del algoritmo genético
    num_individuos = 20 
    num_seleccionados = num_individuos#5
    #origen = "A"
    #destino = "Q"
    
    num_generaciones = 100
    
    tasa_mutacion = 0.1
    
    poblacionG, mejor_individuo, mejor_costo, x, it  = algoritmo_genetico(num_individuos, origen, destino, tasa_mutacion, num_generaciones)
    
    print("")
    print("")
    print("RESULTADO")
    print("--------------")
    # Imprimir la mejor solución encontrada
    #print("Poblacion Final: ", poblacionG)
    print("Numero de iteraciones el mejor: ",it)
    print("Mejor solucionn encontrada:", mejor_individuo)
    print("Numero de iteraciones: ",x)
    print("Mejor costo: ",mejor_costo)
    
    return mejor_individuo
    
# general("A", "C")