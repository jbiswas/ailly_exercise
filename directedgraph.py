class DirectedGraph:
    
    def __init__(self, vertices, edges):
        self.edges = edges
        self.vertices = vertices

    def get_number_of_edges(self):
        return len(self.edges)

    def get_number_of_vertices(self):
        return len(self.vertices)
    
    def get_indegrees(self, vertex):
        return len(list(filter(lambda x: x[1] == vertex, self.edges)))
    
    def get_outdegrees(self, vertex):
        return len(list(filter(lambda x: x[0] == vertex, self.edges)))