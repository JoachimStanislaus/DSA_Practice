# Breath First Search - Graph Algo
# Explores layer by layer
from collections import deque

def BFS(graph, node):
    visited = []
    queue = deque()

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.popleft()
        print(s, end = " ")

        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

# Creating a graph as an adjacency list using a dictionary
graph = {
    "A": ["B", "C"],  # Node A is connected to B and C
    "B": ["D"],       # Node B is connected to D
    "C": ["E"],       # Node C is connected to E
    "D": ["F"],       # Node D is connected to F
    "E": ["F"],       # Node E is also connected to F
    "F": []           # Node F has no outgoing edges
}

BFS(graph, 'A')



