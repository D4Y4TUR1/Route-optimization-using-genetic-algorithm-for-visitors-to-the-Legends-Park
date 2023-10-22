import random
import getrutasintermedia_rr_1 as rr1
import getrutasintermedia_sr_1 as sr1

import getnodosadyascente_1 as ad
import txt_1 as txt


def juntar(origen, destino):
    cantidad = 3
    rr = rr1.rutas_intermedias_x_cantidad_rr_quitando_final(origen, destino, cantidad)
    sr = sr1.rutas_intermedias_x_cantidad_sr_quitando_final(origen, destino, cantidad)
    
    total = sr + rr
    total_sin_repetir = list(map(list, set(map(tuple, total))))
    
    return total_sin_repetir


def metodo_mutacion(individuo, tasa_mutacion):
    for i in range(1,len(individuo)-1):
        # print("##")
        if random.random() < tasa_mutacion:
            origen = individuo[i-1]
            destino = individuo[i+1]
            
            if(origen == destino):
                # print("Problema1")
                #Utilizar Adyascente
                ruta = ad.lugares_interconectados(origen)
                indice = random.randint(0,len(ruta)-1)
                individuo[i] = ruta[indice]
                # print("Problema1: ", individuo[i])
                # print("Problema1: ", individuo)
            else:
                array = juntar(origen,destino)
                # print("Array: ", array)
                
                
                if(len(array)==1):
                    # print("Problema2")
                    # #indice = random.randint(0,len(array)-1)
                    individuo[i] = array[0][1]#array[indice]#random.randint(1,8)  # Cambia el n° de 1 a 8
                    # print("Problema2: ", individuo[i])
                    # print("Problema2: ", individuo)
                else:
                    if(len(array)!=0):
                        # print("Problema3")
                        indiceR = random.randint(0,len(array)-1)
                        ruta1=array[indiceR]
                        # print("R: ", ruta1)
                        # # indice = random.randint(0,len(ruta1)-1)
                        ruta2= ruta1[1]#ruta1[indice]
                        
                        individuo[i] = ruta2
                        # print("Problema3: ", individuo[i])
                        # print("Problema3: ", individuo)                        
                    # else:
                    #     print()#print("Esta mal")
    return individuo


def mutacion_flip_bit(poblacion, tasa_mutacion):
    m = poblacion
    
    for i in range(len(poblacion)):
         m[i] = metodo_mutacion(m[i], tasa_mutacion)
    
    poblacion = m
    
    return poblacion


def mutacion(poblacion, tasa_mutacion):
    m = poblacion
    
    m = mutacion_flip_bit(m, tasa_mutacion)
    
    poblacion = m
    
    return poblacion


# tasa_mutacion = 0.9
# individuo = ['H', 'NC7', 'NC11', 'NC12']
# poblacion = [['A', 'Z', 'A', 'NC15', 'Q'], ['A', 'NC14', 'A', 'NC15', 'Q'], ['A', 'NC14', 'A', 'NC15', 'Q']]
# m = mutacion(poblacion, tasa_mutacion)#metodo_mutacion(individuo, tasa_mutacion)
# print(m)
    


# individuo= ['A', 'B', 'C', 'B','D', 'E']
# tasa_mutacion = 0.9

# individuo= mutacion_flip_bit(individuo, tasa_mutacion)
# print(individuo)
    

# poblacion = [['A', 'Z', 'A', 'NC15', 'Q'], ['A', 'NC14', 'A', 'NC15', 'Q'], ['A', 'NC14', 'A', 'NC15', 'Q']]
# tasa_mutacion = 0.9
# p = mutacion(poblacion, tasa_mutacion)
# print(p)
    