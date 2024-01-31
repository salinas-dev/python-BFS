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
            solucionado = True
            return nodo
        else:
            #Expandir los nodo_hijo
            dato_nodo = nodo.get_datos()
            #Array = Poque la lista de hijos va ser def
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo)
         
            nodo.set_hijos(lista_hijos)
            # Ordenar la lista de nodos_frontera por distancia y volumetría
            nodos_frontera.sort(key=lambda x: (calcular_distancia(conexiones, x.get_datos(), solucion), calcular_volumetria(x.get_datos())))

    return None

def calcular_distancia(conexiones, origen, destino):
    # Calcular la distancia entre dos ciudades
    distancia = 0
    ciudad_actual = origen
    while ciudad_actual != destino:
        ciudad_siguiente = min(conexiones[ciudad_actual], key=lambda x: calcular_distancia_entre_ciudades(ciudad_actual, x))
        distancia += calcular_distancia_entre_ciudades(ciudad_actual, ciudad_siguiente)
        ciudad_actual = ciudad_siguiente
    return distancia

def calcular_distancia_entre_ciudades(ciudad1, ciudad2):
    # Tabla de distancias entre ciudades
    distancias = {
        ('CDMX', 'SLP'): 400,
        ('CDMX', 'MEXICALI'): 2600,
        ('CDMX', 'CHIHUAHUA'): 1450,
        ('SAPOPAN', 'ZACATECAS'): 220,
        ('SAPOPAN', 'MEXICALI'): 2380,
        ('GUADALAJARA', 'CHIAPAS'): 1350,
        ('CHIAPAS', 'CHIHUAHUA'): 1650,
        ('MEXICALI', 'SONORA'): 320,
        ('SLP', 'MEXICALI'): 2480,
        ('ZACATECAS', 'SONORA'): 1050,
        ('ZACATECAS', 'CHIHUAHUA'): 420,
        ('MICHOACAN', 'CHIHUAHUA'): 1650,
        ('CHIHUAHUA', 'MEXICALI'): 1400,
        ('CHIHUAHUA', 'ZACATECAS'): 420,
        ('CHIHUAHUA', 'CDMX'): 1450,
    }
    return distancias.get((ciudad1, ciudad2), float('inf'))

def calcular_volumetria(ciudad):
    # Tabla de volúmenes en metros cúbicos
    tabla_volumetria = {
    'CDMX': 20000,
    'SAPOPAN': 15000,
    'GUADALAJARA': 10000,
    'CHIAPAS': 12000,
    'MEXICALI': 22000,
    'SLP': 17000,
    'ZACATECAS': 18000,
    'SONORA': 19000,
    'MICHOACAN': 9000,
    'CHIHUAHUA': 21000
    }
    return tabla_volumetria[ciudad]

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodos_frontera.append(nodo_inicial)
    while (not solucionado) and len(nodos_frontera) != 0:
        # Ordenar los nodos frontera según la suma de la distancia y la volumetría
        nodos_frontera = sorted(nodos_frontera, key=lambda x: x.get_costo(), reverse=False)
        nodo = nodos_frontera[0]
        # Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos() == solucion:
        # Solución encontrada
            solucionado = True
            return nodo
        else:
        # Expandir los nodo_hijo
            dato_nodo = nodo.get_datos()
            lista_hijos = []
        for un_hijo in conexiones[dato_nodo]:
            hijo = Nodo(un_hijo)
            # Calcular la distancia y la volumetría desde el nodo padre al nodo hijo
            distancia = calcular_distancia(dato_nodo, un_hijo)
            volumetria = calcular_volumetria(un_hijo)
            # Calcular el costo total desde el nodo inicial hasta el nodo hijo
            costo = nodo.get_costo() + distancia + volumetria
            # Establecer el costo del nodo hijo y añadirlo a la lista de hijos
            hijo.set_costo(costo)
            lista_hijos.append(hijo)
        if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
            nodos_frontera.append(hijo)
            nodo.set_hijos(lista_hijos)
    
    return None
    
if __name__ == "__main__":
    # Lista con un diccionario
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

    #Calcular ruta óptima por distancia
    resultado_distancia = []
    nodo_distancia = nodo_solucion
    distancia_total = 0

    while nodo_distancia.get_padre() != None:
        resultado_distancia.append(nodo_distancia.get_datos())
        padre = nodo_distancia.get_padre()
        distancia_total += conexiones[padre.get_datos()][nodo_distancia.get_datos()]['distancia']
        nodo_distancia = padre

    resultado_distancia.append(estado_inicial)
    resultado_distancia.reverse()

    # Calcular ruta óptima por volumetría
    resultado_volumetria = []
    nodo_volumetria = nodo_solucion
    volumetria_total = 0

    while nodo_volumetria.get_padre() != None:
        resultado_volumetria.append(nodo_volumetria.get_datos())
        padre = nodo_volumetria.get_padre()
        volumetria_total += calcular_volumetria(padre.get_datos(), nodo_volumetria.get_datos())
        nodo_volumetria = padre

    resultado_volumetria.append(estado_inicial)
    resultado_volumetria.reverse()

    # Imprimir resultados
    print("Ruta óptima por distancia: ", resultado_distancia)
    print("Distancia total recorrida: ", distancia_total)
    print("Ruta óptima por volumetría: ", resultado_volumetria)
    print("Volumetría total transportada: ", volumetria_total)

