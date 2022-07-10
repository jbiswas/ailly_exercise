"""Directed Graph implementation for Ailly"""

class DirectedGraph:
    """Directed Graph using Adjacency Set. Use pickle to serialize/deserialize"""

    def __init__(self, vertices, edges):
        self_adjacent = lambda edge: edge[0] == edge[1]
        missing_vertex = lambda edge: edge[0] not in vertices or edge[1] not in vertices

        if any(filter(lambda edge: missing_vertex(edge) or self_adjacent(edge), edges)):
            raise ValueError

        self.graph = dict.fromkeys(vertices)

        for vertex in self.graph:
            self.graph[vertex] = set()

        for edge in edges:
            self.graph[edge[0]].add(edge[1])

    def get_number_of_edges(self):
        """Returns total number of edges in the graph"""
        return sum(list(map(len, self.graph.values())))

    def get_number_of_vertices(self):
        """Returns total number of vertices in the graph"""
        return len(self.graph)

    def get_indegrees(self, vertex):
        """Returns indegrees of vertex in graph.
           Expects caller to know if vertex exists in graph"""
        return len(list(filter(lambda edges: vertex in edges, self.graph.values())))

    def get_outdegrees(self, vertex):
        """Returns outdegrees of vertex in graph.
           Expects caller to know if vertex exists in graph"""
        return len(self.graph[vertex])
