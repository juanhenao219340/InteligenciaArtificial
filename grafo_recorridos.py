from collections import deque

grafo = {
    'A': {'B': 2, 'C': 20},
    'B': {'D': 2, 'E': 5},
    'C': {'D': 1, 'F': 20},
    'D': {'F': 10},
    'E': {'F': 2},
    'F': {}
}

def sucesores(nodo):
    return list(grafo[nodo].keys())

def bfs_recorrido(inicio):
    cola = deque([inicio])
    visitados = set()
    orden = []
    paso = 0
    while cola:
        actual = cola.popleft()
        print(f"Paso {paso} (BFS):")
        print(f"  Nodo actual: {actual}")
        print(f"  Cola: {list(cola)}")
        print(f"  Visitados: {sorted(list(visitados))}")
        if actual not in visitados:
            visitados.add(actual)
            orden.append(actual)
            for sucesor in sucesores(actual):
                if sucesor not in visitados and sucesor not in cola:
                    cola.append(sucesor)
        paso += 1
    return orden

def dfs_recorrido(inicio):
    pila = [inicio]
    visitados = set()
    orden = []
    paso = 0
    while pila:
        actual = pila.pop()
        print(f"Paso {paso} (DFS):")
        print(f"  Nodo actual: {actual}")
        print(f"  Pila: {list(pila)}")
        print(f"  Visitados: {sorted(list(visitados))}")
        if actual not in visitados:
            visitados.add(actual)
            orden.append(actual)
            for sucesor in reversed(sucesores(actual)):
                if sucesor not in visitados and sucesor not in pila:
                    pila.append(sucesor)
        paso += 1
    return orden

# Probar desde A
inicio = 'A'
print('Recorrido BFS:')
print(bfs_recorrido(inicio))
print('\nRecorrido DFS:')
print(dfs_recorrido(inicio))
