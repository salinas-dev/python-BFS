# Viaje por Carretera con Busqueda de costo Uniforme
import functools
from arbol import Nodo

# x es el coste y y es el nodo de salida
def compara(x, y):
    return x.get_costo() - y.get_costo()

def buscar_solucion_UCS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_costo(0)
    nodos_frontera.append(nodo_inicial)
    while (not solucionado) and len(nodos_frontera) != 0:
        # Ordenar la lista de nodos_frontera
        nodos_frontera = sorted(nodos_frontera, key = functools.cmp_to_key(compara))
        nodo = nodos_frontera[0]
        # Extraer Nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos() == solucion:
            # Solucion Encontrada
            solucionado = True
            return nodo
        else:
            # Expandir nodos hijo (Ciudades con conexiones)
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                coste = conexiones[dato_nodo][un_hijo]
                hijo.set_costo(nodo.get_costo() + costo)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados):
                    # Si esta en la lista, lo sustituimos con el nuevo valor del coste si es menor
                    if hijo.en_lista(nodos_frontera):
                        for n in nodos_frontera:
                            if n.igual(hijo) and n.get_costo() > hijo.get_costo():
                                nodos_frontera.remove(n)
                                nodos_frontera.append(hijo)
                    else:
                        nodos_frontera.append(hijo)
                nodo.set_hijos(lista_hijos)

if __name__ == '__main__':
    conexiones = {
        'EDO.MEX' : {'CDMX' : 125, 'SLP' : 513},
        'Puebla' : {'SLP' : 514},
        'CDMX' : {'EDO.MEX' : 125, 'SLP' : 423, 'Monterrey' : 491},
        'Michoacan' : {'CDMX' : 491, 'SLP' : 355, 'Monterrey' : 309, 'Sonora' : 346},
        'SLP' : {'Queretaro' : 203, 'Puebla' : 514, 'EDO.MEX' : 513, 'CDMX' : 423, 'Michoacan' : 355, 'Sonora' : 603, 'Monterrey' : 313, 'Guadalajara' : 437, 'Hidalgo' : 599},
        'Queretaro' : {'Hidalgo' : 390, 'SLP' : 203},
        'Hidalgo' : {'Queretaro' : 390, 'SLP' : 599},
        'Guadalajara' : {'SLP' :437, 'Monterrey' : 394},
        'Monterrey' : {'Sonora' : 296,'Michoacan' : 309,'SLP' : 313, "Guadalajara" : 394},
        'Sonora' : {'Monterrey' : 296, 'SLP' : 603, 'Michoacan' : 346}
    }

    estado_inicial = 'EDO.MEX'
    solucion = 'Hidalgo'
    nodo_solucion = buscar_solucion_UCS(conexiones, estado_inicial, solucion)

    # Mostrar Resultados
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    print('Costo: ' + str(nodo_solucion.get_costo()))

