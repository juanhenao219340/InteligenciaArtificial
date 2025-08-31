
from collections import deque

def es_valido(estado):
    P, L, C, O = estado
    # El lobo no puede quedarse solo con la cabra
    if L == C and P != L:
        return False
    # La cabra no puede quedarse sola con la col
    if C == O and P != C:
        return False
    return True

def mover(estado, quien):
    P, L, C, O = estado
    nuevo_P = "D" if P == "I" else "I"

    if quien == "P":
        return (nuevo_P, L, C, O)
    elif quien == "L" and P == L:
        return (nuevo_P, nuevo_P, C, O)
    elif quien == "C" and P == C:
        return (nuevo_P, L, nuevo_P, O)
    elif quien == "O" and P == O:
        return (nuevo_P, L, C, nuevo_P)
    return None

def sucesores(estado):
    posibles = []
    for quien in ["P", "L", "C", "O"]:
        nuevo_estado = mover(estado, quien)
        if nuevo_estado and es_valido(nuevo_estado):
            posibles.append(nuevo_estado)
    return posibles

def bfs_pastor(inicio, meta):
    cola = deque([[inicio]])
    visitados = set()

    while cola:
        camino = cola.popleft()
        estado = camino[-1]

        if estado == meta:
            return camino

        if estado not in visitados:
            for sucesor in sucesores(estado):
                nuevo_camino = list(camino)
                nuevo_camino.append(sucesor)
                cola.append(nuevo_camino)
            visitados.add(estado)
    return None

def dfs_pastor(inicio, meta):
    pila = [[inicio]]
    visitados = set()

    while pila:
        camino = pila.pop()
        estado = camino[-1]

        if estado == meta:
            return camino

        if estado not in visitados:
            for sucesor in sucesores(estado):
                nuevo_camino = list(camino)
                nuevo_camino.append(sucesor)
                pila.append(nuevo_camino)
            visitados.add(estado)
    return None

# Probar
inicio = ("I","I","I","I")
meta   = ("D","D","D","D")
sol = bfs_pastor(inicio, meta)
print("Solución encontrada (BFS):")
for paso in sol:
    print(paso)

sol_dfs = dfs_pastor(inicio, meta)
print("\nSolución encontrada (DFS):")
for paso in sol_dfs:
    print(paso)
 