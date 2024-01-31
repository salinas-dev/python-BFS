#Vuelos con busqueda en amplitud
from arbol import Nodo

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inical = Nodo(estado_inicial)
    nodos_frontera.append(nodo_inical)
    while (not solucionado) and len(nodos_frontera) != 0:
        nodo = nodos_frontera[0]
        #Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos() == solucion:
            #Solucion encontrada
            solucion = True
            return nodo
        else:
            #Expandir los nodo_hijo
            dato_nodo = nodo.get_datos()
            #Array = Poque la lista de hijos va ser def
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados)\
                    and not hijo.en_lista(nodos_frontera):
                        nodos_frontera.append(hijo)
         
        nodo.set_hijos(lista_hijos)
        
    return None
        
if __name__ == "__main__":
        #Lista con un diccionario
    conexiones = {
        'CDMX': {'SLP','MEXICALI','CHIHUAHUA'},
        'SAPOPAN': {'ZACATECAS','MEXICALI'},
        'GUADALAJARA':{'CHIAPAS'},
        'CHIAPAS':{'CHIHUAHUA'},
        'MEXICALI':{'SLP','SAPOPAN','CDMX','CHIHUAHUA','SONORA'},
        'SLP':{'CDMX','MEXICALI'},
        'ZACATECAS':{'SAPOPAN','SONORA','CHIHUAHUA'},  
        'SONORA':{'ZACATECAS','MEXICALI'},
        'MICHOACAN':{'CHIHUAHUA'},
        'CHIHUAHUA':{'MICHOACAN','ZACATECAS','MEXICALI','CDMX','CHIAPAS'}
    }
    
    estado_inicial = 'CDMX'
    solucion = 'ZACATECAS'
    nodo_solucion = buscar_solucion_BFS(conexiones, estado_inicial, solucion)
    #Mostrar resultado es igual a una lista
    #resultado es igual a una lista
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() !=None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
        
    resultado.append(estado_inicial)
    resultado.reverse()
    print (resultado)
