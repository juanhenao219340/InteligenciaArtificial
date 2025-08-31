from collections import deque

def es_valido(estado):
    # Estado válido si los valores están dentro de los límites de las jarras
    jarra5, jarra3 = estado
    return 0 <= jarra5 <= 5 and 0 <= jarra3 <= 3

def sucesores(estado):
    jarra5, jarra3 = estado
    posibles = []
    # Llenar jarra de 5L
    posibles.append((5, jarra3))
    # Llenar jarra de 3L
    posibles.append((jarra5, 3))
    # Vaciar jarra de 5L
    posibles.append((0, jarra3))
    # Vaciar jarra de 3L
    posibles.append((jarra5, 0))
    # Verter de 5L a 3L
    transfer = min(jarra5, 3 - jarra3)
    posibles.append((jarra5 - transfer, jarra3 + transfer))
    # Verter de 3L a 5L
    transfer = min(jarra3, 5 - jarra5)
    posibles.append((jarra5 + transfer, jarra3 - transfer))
    # Filtrar solo estados válidos
    return [e for e in posibles if es_valido(e)]

def bfs(inicio, meta):
    cola = deque([[inicio]])
    visitados = set()
    visitados_orden = []

    while cola:
        camino = cola.popleft()
        estado = camino[-1]

        if estado == meta:
            return camino, visitados_orden

        if estado not in visitados:
            visitados.add(estado)
            visitados_orden.append(estado)
            for sucesor in sucesores(estado):
                nuevo_camino = list(camino)
                nuevo_camino.append(sucesor)
                cola.append(nuevo_camino)
    return None, visitados_orden

def dfs(inicio, meta):
    pila = [[inicio]]
    visitados = set()
    visitados_orden = []

    while pila:
        camino = pila.pop()
        estado = camino[-1]

        if estado == meta:
            return camino, visitados_orden

        if estado not in visitados:
            visitados.add(estado)
            visitados_orden.append(estado)
            for sucesor in sucesores(estado):
                nuevo_camino = list(camino)
                nuevo_camino.append(sucesor)
                pila.append(nuevo_camino)
    return None, visitados_orden


# Probar
inicio = (0, 0)
meta = (4, 0)
sol_bfs, visitados_bfs = bfs(inicio, meta)
print("Solución encontrada (BFS):")
for paso in sol_bfs:
    print(paso)
print("\nEstados visitados por BFS:")
for i, estado in enumerate(visitados_bfs):
    print(f"{i}: {estado}")

sol_dfs, visitados_dfs = dfs(inicio, meta)
print("\nSolución encontrada (DFS):")
for paso in sol_dfs:
    print(paso)
print("\nEstados visitados por DFS:")
for i, estado in enumerate(visitados_dfs):
    print(f"{i}: {estado}")
