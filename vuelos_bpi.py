# Vuelos con búsqueda con profundidad iterativa
from arbol import Nodo

def DFS_prof_iter(nodo,solucion):
    # Ciclo que va de 0 a  100.
    for limite in range(0,100):
        visitados = []
        sol = buscar_solucion_DFS_Rec(nodo, solucion, visitados, limite)
        if sol != None:
            return sol

def buscar_solucion_DFS_Rec(nodo, solucion, visitados, limite):
    if limite > 0:
        visitados.append(nodo)
        if nodo.get_datos() == solucion:
            return nodo
        else:
            # Expandir nodos_hijo (ciudades con Conexión)
            dato_nodo = nodo.get_datos()
            lista_hijos = []

            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                if not hijo.en_lista(visitados):
                    lista_hijos.append(hijo)
        
            nodo.set_hijos(lista_hijos)
        
            for nodo_hijo in nodo.get_hijos():
                if not nodo_hijo.get_datos() in visitados:
                    # Llamada Recursiva
                    sol = buscar_solucion_DFS_Rec(nodo_hijo, solucion, visitados, limite-1)
                    if sol != None:
                        return sol
        return None


if __name__ == '__main__':
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
    nodo_inicial = Nodo(estado_inicial)
    nodo = DFS_prof_iter(nodo_inicial, solucion)

    # Mostrar Resultados
    if nodo !=None:
        resultado = []
        while nodo.get_padre() != None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()
        print(resultado)
    else:
        print("Solución no encontradas")
