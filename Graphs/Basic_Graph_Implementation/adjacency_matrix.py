# How a graph using an adjacency matrix looks like:
"""
   0  1  2  3
0 [0, 1, 0, 1]
1 [1, 0, 1, 0]
2 [0, 1, 0, 1]
3 [1, 0, 1, 0]
"""

# Implement a graph using an adjacency matrix.
class Graph:
    def __init__(self, num_vertices):
        """ Initialize the graph with a given number of vertices """
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]


# Implement a function to add and remove edges in a graph.
    def add_edge(self, u, v, weight=1):
        """ Add an edge from vertex u to vertex v with an optional weight (default 1). """
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight # If graph undirected, if directed, remove.
    
    def remove_edge(self, u, v):
        """Remove the edge between vertex u and vertex v."""
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0 # If graph undirected, if directed, remove.
        
    def print_graph(self):
        """Print the adjacency matrix of the graph."""
        for row in self.adj_matrix:
            print(row)

# Implement a function to check if an edge exists between two nodes.
    def has_edge(self, u, v):
        """Check if theere is an edge between vertex u and vertex v"""
        return self.adj_matrix[u][v] != 0 

# Implement a function to find the degree of a node. (refers to how many edges are connected to it)
    def node_degree(self,node):
        count=0
        for x in self.adj_matrix[node]:
            if x > 0:
                count+=1
        return count

g = Graph(4)  # 4 vertices (0, 1, 2, 3)
g.add_edge(0, 1)  # Edge from 0 to 1
g.add_edge(1, 2)  # Edge from 1 to 2
g.add_edge(2, 3)  # Edge from 2 to 3
g.add_edge(3, 0)  # Edge from 3 to 0

g.print_graph()
print(g.node_degree(0))