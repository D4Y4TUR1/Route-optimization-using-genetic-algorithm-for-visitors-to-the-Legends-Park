import random

def padre1_segmento(padre):
    segmento1 = [None] * len(padre)
    segmento2 = [None] * len(padre)
    
    
    tamano_cromosoma = len(padre)
    
    punto_inicio = random.randint(1, tamano_cromosoma - 2)
    punto_fin = random.randint(punto_inicio, tamano_cromosoma - 2)
    
    ini = punto_inicio
    fin = punto_fin
    origen = padre[punto_inicio-1]
    destino = padre[punto_fin+1]
    # print("PI: ",ini)
    # print("PF: ", fin)
    # print("Origen: ", origen)
    # print("Destino: ", destino)
    
    cantidad = punto_fin - punto_inicio + 1 + 2
    # print("Cantidad: ", cantidad)
    
    segmento1[punto_inicio:punto_fin + 1] = padre[punto_inicio:punto_fin + 1]
    segmento2[0:punto_inicio] = padre[0:punto_inicio]
    segmento2[punto_fin + 1:len(padre)] = padre[punto_fin + 1:len(padre)]
    
    # print(segmento1)
    # print(segmento2)
    
    segmento = segmento2
    guardar = segmento1
    
    return segmento, guardar, origen, destino,ini,fin, cantidad

# padre1 = [1,2,3,4,5,6,7]#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# s,g,o,d,i,f,c = padre1_segmento(padre1)

# s[i:f+1] = g[i:f+1]

# print(s)