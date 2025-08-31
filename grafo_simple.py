from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E', 'G'],
    'C': ['F', 'H'],
    'D': ['I', 'O'],
    'E': ['J', 'K'],
    'F': ['P'],
    'G': ['L'],
    'H': ['N'],
    'I': ['Q'],
    'J': [],
    'K': ['R'],
    'L': ['S'],
    'M': ['T'],
    'N': ['M'],
    'O': ['V'],
    'P': ['W'],
    'Q': ['X'],
    'R': ['Y'],
    'S': ['Z'],      
    'T': ['U'],
    'U': ['Z'],
    'V': [],
    'W': ['Z'],
    'X': [],
    'Y': ['Z'],
    'Z': []
}

def bfs(start, end, graph):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == end:
            return path
        
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                queue.append(path + [neighbor])
    return None

def dfs(start, end, graph):
    visited = set()
    stack = [[start]]

    while stack:
        path = stack.pop()
        current = path[-1]

        if current == end:
            return path
        
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                stack.append(path + [neighbor])
    return None

print("BFS:", bfs('A', 'Z', graph))
print("DFS:", dfs('A', 'Z', graph))