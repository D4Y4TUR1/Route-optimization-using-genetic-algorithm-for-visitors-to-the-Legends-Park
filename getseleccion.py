import random
import fitness as f

def seleccion_ruleta(poblacion, num_seleccionados):
    # Calcular la aptitud total de la población
    aptitud_total = sum([f.fitness_3v(ruta) for ruta in poblacion])#sum([f.calcular_aptitud(ruta) for ruta in poblacion])
    #print("Aptitud: ", aptitud_total)
    
    # Calcular la probabilidad de selección para cada individuo
    probabilidades = [f.fitness_3v(ruta) / aptitud_total for ruta in poblacion]#[f.calcular_aptitud(ruta) / aptitud_total for ruta in poblacion]
    #print("Probabilidad: ", probabilidades)
    
    pob = poblacion.copy()
    pro = probabilidades.copy()
    
    seleccionados = []
    repetidosSEL = []
    #print("Se hace copia de: ", poblacion)
    # Realizar la selección de individuos
    
    repetida = (int) ((num_seleccionados)*0.25)
    for i in range(num_seleccionados):
        #print("P: ", pob)
        indice = random.choices(range(len(pob)), weights=pro, k=1)[0]
        elemento = pob[indice]
        seleccionados.append(elemento)
        repetidosSEL.append(elemento)
        repetida = contar_repeticiones(elemento, repetidosSEL)
        if(repetida == repetida):
            #print("ELIMINADO: ", elemento)
            pob.remove(elemento)
            pro.remove(pro[indice])
            repetidosSEL = []
        
    return seleccionados

def contar_repeticiones(elemento, lista):
    contador = 0

    for diccionario in lista:
        if diccionario == elemento:
            contador += 1

    return contador