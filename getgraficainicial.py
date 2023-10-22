import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import getdatos_1 as d

def grafica_inicial():
    # Lista de lugares
    lugares = d.getLugares_Completo()
    #print("LUGARES: ", lugares[0])
    
    # Matriz de adyacencia
    matriz_adyacencia = d.getMatrizAdyacencia_Completa()
    
    # Coordenadas para los lugares en el diagrama de dispersión
    coordenadas_x, coordenadas_y = d.getCoordenadas()
    
    # Ruta de la imagen a agregar
    ruta_imagen = "grafica_leyenda_1.png"
    
    # Cargar la imagen
    imagen = mpimg.imread(ruta_imagen)
    
    # Crear una figura y un eje
    fig, ax = plt.subplots()
    #Pintar de rojo los puntos
    coordenadas_x_pt1 = coordenadas_x[:26]
    coordenadas_y_pt1 = coordenadas_y[:26]
    ax.scatter(coordenadas_x_pt1, coordenadas_y_pt1, color='red', s=120) 
    
    
    #Pintar azul los puntos
    coordenadas_x_pt2 = coordenadas_x[26:]
    coordenadas_y_pt2 = coordenadas_y[26:]
    ax.scatter(coordenadas_x_pt2, coordenadas_y_pt2, color='blue', s=120) 
    
    
    
    #Graficar las conexiones definidas en la matriz de adyacencia
    for i in range(len(lugares)):
            
        for j in range(i+1, len(lugares)):
            if matriz_adyacencia[i][j] == 1:
                ax.plot([coordenadas_x[i], coordenadas_x[j]], [coordenadas_y[i], coordenadas_y[j]], color='black')#color='gray'
    
    # Configurar los límites del eje x y y
    ax.set_xlim(0, 60)
    ax.set_ylim(0, 60)
    
    # Agregar la imagen como fondo
    ax.imshow(imagen, extent=[0, 60, 0, 60], aspect='auto')
    
    # Agregar etiquetas de los ejes
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    
    # Agregar título al gráfico
    ax.set_title('Gráfico de lugares con imagen de fondo')
    
    # Generar la leyenda fuera del gráfico
    #plt.legend(lugares, loc='upper left', bbox_to_anchor=(1, 1))
    #Sin lineas
    #plt.legend(lugares, loc='upper left', bbox_to_anchor=(1, 1), labelspacing=0)
    
    #plt.legend(lugares, loc='upper left', bbox_to_anchor=(1, 1), handlelength=0)
    
    # Mostrar el gráfico
    plt.show()
    
# grafica_inicial()


