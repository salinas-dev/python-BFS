import heapq
from arbol import Nodo  # Importar el módulo Nodo desde el archivo arbol.py

# Definir las ciudades y sus ubicaciones
ciudades = {
    'SLP': (22.1565, -100.9855),  # Ciudad: (latitud, longitud)
    'HIDALGO': (19.6833, -100.5833),
    'QRO': (20.5881, -100.3881),
    'PUEBLA': (19.0414, -98.2063),
    'EDOMEX': (19.2879, -99.6536),
    'CDMX': (19.4326, -99.1332),
    'MICHOACAN': (19.8634, -103.0233),
    'SONORA': (32.7117, -114.8161),
    'MONTERREY': (25.6866, -100.3161),
    'GUADALAJARA': (20.6597, -103.3496)
}

# Definir las conexiones entre las ciudades
conexiones = {
    'SLP': ['GUADALAJARA', 'MONTERREY', 'MICHOACAN', 'CDMX', 'EDOMEX', 'PUEBLA', 'QRO', 'HIDALGO', 'SONORA'],
    'HIDALGO': ['SLP', 'QRO'],
    'QRO': ['HIDALGO', 'SLP'],
    'PUEBLA': ['SLP'],
    'EDOMEX': ['SLP', 'CDMX'],
    'CDMX': ['EDOMEX', 'MICHOACAN', 'SLP'],
    'MICHOACAN': ['SLP', 'CDMX', 'SONORA', 'MONTERREY'],
    'SONORA': ['MICHOACAN', 'SLP', 'MONTERREY'],
    'MONTERREY': ['SONORA', 'SLP', 'MICHOACAN'],
    'GUADALAJARA': ['SLP', 'MONTERREY']
}

# Definir la heurística de distancia Euclidiana
def heuristica(ciudad_actual, ciudad_destino):
    x1, y1 = ciudades[ciudad_actual]
    x2, y2 = ciudades[ciudad_destino]
    return ((x2 - x1) * 2 + (y2 - y1) * 2) ** 0.5

# Implementar el algoritmo de búsqueda A*
def buscar_ruta(ciudad_inicial, ciudad_destino):
    # Inicializar las estructuras de datos
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, ciudad_inicial))
    padres = {}
    g_costo = {ciudad_inicial: 0}

    while cola_prioridad:
        costo_actual, ciudad_actual = heapq.heappop(cola_prioridad)

        if ciudad_actual == ciudad_destino:
            break

        for ciudad_vecina in conexiones[ciudad_actual]:
            nuevo_g_costo = g_costo[ciudad_actual] + 1

            if ciudad_vecina not in g_costo or nuevo_g_costo < g_costo[ciudad_vecina]:
                g_costo[ciudad_vecina] = nuevo_g_costo
                f_costo = nuevo_g_costo + heuristica(ciudad_vecina, ciudad_destino)
                heapq.heappush(cola_prioridad, (f_costo, ciudad_vecina))
                padres[ciudad_vecina] = ciudad_actual

    # Reconstruir la ruta desde la ciudad destino hasta la ciudad inicial
    ruta = [ciudad_destino]
    ciudad_actual = ciudad_destino

    while ciudad_actual != ciudad_inicial:
        ciudad_actual = padres[ciudad_actual]
        ruta.append(ciudad_actual)

    ruta.reverse()
    return ruta

# Validar números complejos y flotantes
def validar_numero(coord):
    try:
        float(coord)
        return True
    except ValueError:
        return False

def validar_coordenadas(ciudades):
    for ciudad, coordenadas in ciudades.items():
        if not all(validar_numero(coord) for coord in coordenadas):
            raise ValueError("Las coordenadas de la ciudad '{}' no son válidas.".format(ciudad))

# Ejemplo de uso
try:
    validar_coordenadas(ciudades)
    ruta_optima = buscar_ruta('SLP', 'QRO')
    print(ruta_optima)
except ValueError as error:
    print("Error:", str(error))
