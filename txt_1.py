import pickle
import os

def leerMTXT(archivo):
    # Leer el array bidimensional existente desde el archivo si existe
    try:
        with open(archivo, "rb") as archivo:
            array_bidimensional_existente = pickle.load(archivo)
    except FileNotFoundError:
        # Si el archivo no existe, inicializa el array bidimensional como vacío
        array_bidimensional_existente = []
    
    return array_bidimensional_existente
        
def guardarMTXT(archivo, nuevos_elementos):

    array_bidimensional_existente = leerMTXT(archivo)
    
    # Agregar los nuevos elementos al array bidimensional existente
    array_bidimensional_actualizado = array_bidimensional_existente + nuevos_elementos
    
    # Guardar el array bidimensional actualizado en el archivo
    with open(archivo, "wb") as archivo:
        pickle.dump(array_bidimensional_actualizado, archivo)
        
    #print(array_bidimensional_actualizado )

def eliminarMTXT(archivo): 
    
    # Verificar si el archivo existe antes de intentar eliminarlo
    if os.path.exists(archivo):
        os.remove(archivo)
        print(f"El archivo {archivo} ha sido eliminado.")
    else:
        print(f"El archivo {archivo} no existe.")
        
def leerDestino():

    archivo = open("nodo_destino.txt", "r")
    contenido = archivo.read()
    archivo.close()
    
    destino = contenido
    
    return destino


def guardarDestino(destino):
    valor = destino

    archivo = open("nodo_destino.txt", "w")
    archivo.write(str(valor))
    archivo.close()

# guardarDestino('Q')

# print(leerDestino())
        
#def generar apoyo_ruta():
    

#print(leerMTXT())
#eliminarMTXT()
    
# # Nuevos elementos a agregar al array bidimensional
# nuevos_elementos = [[4, 5, 6], [7, 8, 9]]

# guardarMTXT(nuevos_elementos)