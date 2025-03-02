# How a graph implemented using an adjacency list looks like:
"""
0: [1, 3]
1: [0, 2]
2: [1, 3]
3: [0, 2]
"""

# Implement a graph using an adjacency list.
class Graph:
    def __init__(self):
        """Initialise an empty adjacency list"""
        self.graph = {}

# Implement a function to add and remove edges in a graph.
    def add_node(self,node):
        """Add a new node to the graph"""
        if node not in self.graph:
            self.graph[node] = []
    
    def add_edge(self,u,v, directed=False):
        """
        Add an edge from node u to node v
        If the graph is undirected, also add an edge from v to u.
        """
        if u not in self.graph:
            self.add_node(u)
        if v not in self.graph:
            self.add_node(v)
        
        self.graph[u].append(v)

        if not directed:
            self.graph[v].append(u)

    def remove_edge(self,u,v,directed=False):
        """
        Remove an edge from node u to node v
        If the graph is undirected, also remove an edge from v to u
        """
        if u in self.graph and v in self.graph:
            self.graph[u].remove(v)
        if not directed and v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)
         
    def remove_node(self,node):
        """Remove a node and all its edges"""
        if node in self.graph:
            # Remove edges from other nodes pointing to this node
            for neighbour in list(self.graph[node]):
                self.graph[neighbour].remove(node)
            del self.graph[node]
        
    def get_neighbours(self,node):
        """Returns a list of neighbours of the given node."""
        return self.graph.get(node,[])

    def display(self):
        """Print the adjacency list of the graph"""
        for node in self.graph:
            print(f'{node}: {self.graph[node]}')

# Implement a function to check if an edge exists between two nodes.
    def check_if_edge_exists(self,u,v,directed=False):
        """Check if edge exists between 2 nodes"""
        if u in self.graph and v in self.graph:
            if directed and v in self.graph[u] and u in self.graph[v]:
                return True
            elif not directed and (v in self.graph[u] or u in self.graph[v]):
                return True
        return False

# Implement a function to find the degree of a node.
    def get_node_degree(self,node):
        """Get the degree of the node(how many nodes connected to it)"""
        if node in self.graph:
            return len(self.graph[node])
        return 0
