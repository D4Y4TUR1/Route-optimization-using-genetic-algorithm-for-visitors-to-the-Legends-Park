def segmentos(padre, origen, final, cantidad):
    segmentos = []
    for i in range(len(padre)):
        if padre[i] == origen:
            for j in range(i+1, len(padre)):
                if padre[j] == final:
                    segmento = padre[i:j+1]
                    # print("segmento: ",segmento)
                    if(cantidad == len(segmento)):
                        segmentos.append(segmento)
    # print("")
    # print("Segmentos encontrados:")
    # for segmento in segmentos:
    #     print(segmento)
        
    # print("")
    # print("SS: ",segmentos)
    
    
    segmentos_sin_repetir = list(map(list, set(map(tuple, segmentos))))
    # print("Segmentos sin repetir: ", segmentos_sin_repetir," LON: ", len(segmentos_sin_repetir))
    
    return segmentos_sin_repetir



# padre2 = ['A', 'B', 'C', 'A', 'E', 'C', 'A', 'B', 'D', 'E']

# origen = "A"#input("Ingrese el lugar de origen: ")
# final = "C"#input("Ingrese el lugar final: ")
# cantidad = 0

# segmentoL = segmentos(padre2, origen, final, cantidad)
# print("")
# print("Segmentos: ", segmentoL)
