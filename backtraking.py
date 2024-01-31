from arbol import Nodo

def backtrack_maximizar(grafo, estado_inicial, objetivo, funcion, solucion_actual=[], mejor_solucion=None):
    if estado_inicial == objetivo:
        valor_actual = funcion(solucion_actual)
        if mejor_solucion is None or valor_actual > funcion(mejor_solucion):
            mejor_solucion = solucion_actual[:]
    else:
        for vecino, peso in grafo[estado_inicial].items():
            if vecino not in solucion_actual:
                solucion_actual.append(vecino)
                mejor_solucion = backtrack_maximizar(grafo, vecino, objetivo, funcion, solucion_actual, mejor_solucion)
                solucion_actual.pop()

    return mejor_solucion

# Ejemplo de uso
def funcion_ejemplo(solucion):
    # Función de ejemplo que suma los pesos de la solución
    return sum([grafo[solucion[i]][solucion[i+1]] for i in range(len(solucion)-1)])

grafo = {
    'SLP': {'GUADALAJARA': 437, 'MONTERREY': 313, 'MICHOACAN': 355, 'CDMX': 423, 'EDOMEX': 513, 'PUEBLA': 514, 'QRO': 203, 'HIDALGO': 599, 'SONORA': 603},
    'HIDALGO': {'SLP': 599, 'QRO': 390},
    'QRO': {'HIDALGO': 390, 'SLP': 202},
    'PUEBLA': {'SLP': 514},
    'EDOMEX': {'SLP': 513, 'CDMX': 125},
    'CDMX': {'EDOMEX': 125, 'MICHOACAN': 491, 'SLP': 425},
    'MICHOACAN': {'SLP': 355, 'CDMX': 491, 'SONORA': 346, 'MONTERREY': 309},
    'SONORA': {'MICHOACAN': 346, 'SLP': 603, 'MONTERREY': 296},
    'MONTERREY': {'SONORA': 296, 'SLP': 313, 'MICHOACAN': 309},
    'GUADALAJARA': {'SLP': 437, 'MONTERREY': 394}
}

estado_inicial = 'EDOMEX'
estado_objetivo = 'HIDALGO'

mejor_solucion_ejemplo = backtrack_maximizar(grafo, estado_inicial, estado_objetivo, funcion_ejemplo)

print("Mejor solución encontrada:", mejor_solucion_ejemplo)
print("Valor máximo:", funcion_ejemplo(mejor_solucion_ejemplo))
