import openpyxl

def read_excel_data_1d(filename, start_cell, end_cell, sheet_name):
    # Cargar el archivo de Excel
    wb = openpyxl.load_workbook(filename)
    
    # Obtener la hoja especificada por su nombre
    sheet = wb[sheet_name]
    
    # Crear un array unidimensional para almacenar los valores de las celdas
    values_1d = []
    
    # Recorrer las filas dentro del rango especificado
    for row in sheet[start_cell:end_cell]:
        # Recorrer las celdas dentro de cada fila
        for cell in row:
            if cell.value is None:
                # Si la celda está vacía, imprimir un mensaje y agregar un valor nulo al array unidimensional
                print("Se encontró una celda vacía.")
                values_1d.append(None)
            else:
                # Agregar el valor de la celda al array unidimensional
                values_1d.append(cell.value)
    
    # Retornar el array unidimensional
    return values_1d

def read_excel_data_2d(filename, start_cell, end_cell, sheet_name):
    # Cargar el archivo de Excel
    wb = openpyxl.load_workbook(filename)
    
    # Obtener la hoja especificada por su nombre
    sheet = wb[sheet_name]
    
    # Crear un array bidimensional para almacenar los valores de las celdas
    values_2d = []
    
    # Recorrer las filas dentro del rango especificado
    for row in sheet[start_cell:end_cell]:
        row_values = []
        # Recorrer las celdas dentro de cada fila
        for cell in row:
            if cell.value is None:
                # Si la celda está vacía, imprimir un mensaje y agregar un valor nulo al array bidimensional
                print("Se encontró una celda vacía.")
                row_values.append(None)
            else:
                # Agregar el valor de la celda al array bidimensional
                row_values.append(cell.value)
        # Agregar la fila al array bidimensional
        values_2d.append(row_values)
    
    # Retornar el array bidimensional
    return values_2d



# filename = "leer_excel_1.xlsx"
# start_cell = "B3"
# end_cell = "D5"
# sheet_name = "Datos"
# data_1d = read_excel_data(filename, start_cell, end_cell, sheet_name)
# print(data_1d)
def getLugares_Nombres():
    filename = "leyenda_v1.xlsx"
    start_cell = "C4"
    end_cell = "C29"#"A29"
    sheet_name = "NODOS"
    data_1d = read_excel_data_1d(filename, start_cell, end_cell, sheet_name)
    # print(data_1d)
    lugares = data_1d
    return lugares


def getLugares():
    filename = "leyenda_v1.xlsx"
    start_cell = "A4"
    end_cell = "A29"#"A29"
    sheet_name = "NODOS"
    data_1d = read_excel_data_1d(filename, start_cell, end_cell, sheet_name)
    # print(data_1d)
    lugares = data_1d
    
    #Pasar a enteros
    # lugares_enteros = [int(x) for x in lugares]
    # lugares = lugares_enteros
    #print(lugares)
    return lugares

def getLugares_Completo():
    filename = "leyenda_v1.xlsx"
    start_cell = "A4"
    end_cell = "A49"#"A29"
    sheet_name = "NODOS"
    data_1d = read_excel_data_1d(filename, start_cell, end_cell, sheet_name)
    # print(data_1d)
    lugares = data_1d
    
    #Pasar a enteros
    # lugares_enteros = [int(x) for x in lugares]
    # lugares = lugares_enteros
    #print(lugares)
    return lugares


def getCoordenadas():
    ##Excel
    filename = "leyenda_v1.xlsx"
    ##Leer Coordenadas X
    start_cell_X = "D4"
    end_cell_X = "D49"#"D29"
    sheet_name_X = "NODOS"
    data_1d_X = read_excel_data_1d(filename, start_cell_X, end_cell_X, sheet_name_X)
    #print(data_1d_X)
    coordenadasX = data_1d_X
    
    #Leer Coordenadas Y
    start_cell_Y = "E4"
    end_cell_Y = "E49"#"E29"
    sheet_name_Y = "NODOS"
    data_1d_Y = read_excel_data_1d(filename, start_cell_Y, end_cell_Y, sheet_name_Y)
    # print(data_1d_Y)
    coordenadasY = data_1d_Y
    
    return coordenadasX, coordenadasY

def getMatrizAdyacencia():
    filename = "leyenda_v1.xlsx"
    start_cell = "H4"
    end_cell = "AG49"
    sheet_name = "NODOS"
    data_2d = read_excel_data_2d(filename, start_cell, end_cell, sheet_name)
    # print(data_2d)
    
    matriz_adyacencia = data_2d
    
    #Pasar a enteros
    # matriz_adyacencia_enteros = [[int(elemento) for elemento in fila] for fila in matriz_adyacencia]
    # matriz_adyacencia = matriz_adyacencia_enteros
    
    return matriz_adyacencia

def getMatrizAdyacencia_Completa():
    filename = "leyenda_v1.xlsx"
    start_cell = "H4"
    end_cell = "BA49"
    sheet_name = "NODOS"
    data_2d = read_excel_data_2d(filename, start_cell, end_cell, sheet_name)
    # print(data_2d)
    
    matriz_adyacencia = data_2d
    
    #Pasar a enteros
    # matriz_adyacencia_enteros = [[int(elemento) for elemento in fila] for fila in matriz_adyacencia]
    # matriz_adyacencia = matriz_adyacencia_enteros
    
    return matriz_adyacencia

# a = getLugares()
# print("A: ", a)
# getLugares()
#getCoordenadas()

# matr= getMatrizAdyacencia()
# print("MATRIZ: ", matr)


#--------------------------------------------------------------#

# # Lista de lugares
# lugares = ["A", "B", "C", "D", "E"]

# Matriz de adyacencia que representa las conexiones entre los lugares
# matriz_adyacencia = [
#     [0, 1, 1, 0, 0],  # A está conectado con B y C
#     [1, 0, 1, 1, 0],  # B está conectado con A, C y D
#     [1, 1, 0, 0, 1],  # C está conectado con A, B y E
#     [0, 1, 0, 0, 1],  # D está conectado con B y E
#     [0, 0, 1, 1, 0]   # E está conectado con C y D
# ]


# coordenada = [
#         [37,21],
#         [2,2],
#         [3,1],
#         [4,2],
#         [5,3]
    
#     ]


