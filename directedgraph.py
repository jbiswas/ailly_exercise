class DirectedGraph:
    
    def __init__(self, vertices, edges):
        self.vertices = set(vertices)
        if len(list(filter(lambda x: x[0]  not in self.vertices or x[1] not in self.vertices or x[0] == x[1], edges))) > 0:
            raise ValueError
        
        self.edges = set(edges)

    def get_number_of_edges(self):
        return len(self.edges)

    def get_number_of_vertices(self):
        return len(self.vertices)
    
    def get_indegrees(self, vertex):
        return len(list(filter(lambda x: x[1] == vertex, self.edges)))
    
    def get_outdegrees(self, vertex):
        return len(list(filter(lambda x: x[0] == vertex, self.edges)))