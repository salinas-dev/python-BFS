class Nodo:
        def __init__(self, datos, hijos=None):
                self.datos = datos
                self.datos = None
                self.padre = None
                self.costo = None
                self.set_hijos(hijos)

        def set_hijos(self, hijos):
                self.hijos = hijos
                if self.hijos != None:
                    for h in self.hijos:
                        h.padre = self

        def get_hijos(self):
            return self.padre
        
        def set_datos(self, datos):
            self.datos = datos

        def set_costo(self, costo):
            self.costo = costo

        def igual(self, nodo):
            if self.get_datos() == nodo.get_datos():
                return True
            else:
                return False
            
        def en_lista(self, lista_nodos):
            en_la_lista = False
            for n in lista_nodos:
                if self.igual(n):
                    en_la_lista = True
            return en_la_lista

        def __str__(self):
            return str(self.get_datos())
        

-----------------------------------------------------------------------


# Puzzle lineal con busqeda en amplitud

from arbol import Nodo
def buscar_solucion_BFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados=[]
    nodos_frontera=[]
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    while (not solucionado) and len(nodos_frontera) !=0:
        nodo=nodos_frontera.pop()
        #Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo)
        if nodo.get_datos() == solucion:
            #Solucion encontrada
            solucionado = True
            return nodo
        
        else:
            #Expandir nodos hijo
            dato_nodo = nodo.get_datos()
        
        #Operador izquierdo
        hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
        hijo_izquierdo = Nodo(hijo)
        if not hijo_izquierdo.en_lista(nodos_visitados)\
             and not hijo_izquierdo.en_lista(nodos_frontera):
             nodos_frontera.append(hijo_izquierdo)

        #Operador centro
        hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
        hijo_centro = Nodo(hijo)
        if not hijo_centro.en_lista(nodos_visitados)\
             and not hijo_centro.en_lista(nodos_frontera):
             nodos_frontera.append(hijo_centro)
        
        #Operador derecho
        hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
        hijo_derecho = Nodo(hijo)
        if not hijo_derecho.en_lista(nodos_visitados)\
             and not hijo_derecho.en_lista(nodos_frontera):
             nodos_frontera.append(hijo_derecho)
        
        nodo.set_hijos([hijo_izquierdo, hijo_centro, hijo_derecho])

    if __name__ == "__main__":
        estado_inicial = [4,2,3,1]
        solucion = [1,2,3,4]
        modo_solucion =buscar_solucion_BFS(estado_inicial, solucion)

        # Resultado Resultado
        resultado = []
        nodo = modo_solucion
        while nodo.get_padre() != None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()
        print(resultado)