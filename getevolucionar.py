import getseleccion as s

import getcruzamiento as c

import getmutacion as m

def evolucionar_poblacion(poblacion, num_individuos, tasa_mutacion, x):
    #SELECCION
    #print("")
    #print("SELECCION ", (x),)
    #print("---------------")
    seleccionados = s.seleccion_ruleta(poblacion, num_individuos)#, fitness, num_seleccionados);
    #print("SEL: ", seleccionados)
    
    #print("")
    #print("CRUZAMIENTO ", (x))
    #print("----------------")
    cruz = c.cruzamiento(seleccionados)
    #print("CRUX: ", cruz)
    
    
    #print("CCCC: ", len(cruz))
    
    #print("")
    #print("MUTACION ", (x))
    #print("----------------")
    mut = m.mutacion(cruz, tasa_mutacion)
    #print("MUT: ",  mut)
    
    # poblacionfinal = mut
    return mut#poblacionfinal#cruz

# p = [['A', 'NC15', 'A', 'NC15', 'Q'], ['A', 'NC14', 'A', 'NC15', 'Q'], ['A', 'NC15', 'A', 'NC15', 'Q']]

# z = evolucionar_poblacion(p,3,0.9,1)