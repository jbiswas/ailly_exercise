"""Directed Graph implementation for Ailly"""
class DirectedGraph:
    """Directed Graph using Adjacency Set"""

    def __init__(self, vertices, edges):
        if any(filter(lambda x: x[0] not in vertices or x[1] not in vertices or x[0] == x[1], edges)):
            raise ValueError

        self.graph = dict.fromkeys(vertices)

        for vertex in self.graph:
            self.graph[vertex] = set()

        for edge in edges:
            self.graph[edge[0]].add(edge[1])

    def get_number_of_edges(self):
        """Returns total number of edges in the graph"""
        edges = 0
        for vertex in self.graph:
            edges += len(self.graph[vertex])
        return edges

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
        