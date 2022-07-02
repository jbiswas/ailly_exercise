import unittest
import pickle

from directedgraph import DirectedGraph

class DirectedGraphTest(unittest.TestCase):

    def test_empty_graph_returns_zero_edges(self):
        graph = DirectedGraph([], [])
        self.assertEquals(0, graph.get_number_of_edges())

    def test_graph_with_one_edge(self):
        graph = DirectedGraph([1, 2], [(1,2)])
        self.assertEquals(1, graph.get_number_of_edges())
        self.assertEquals(2, graph.get_number_of_vertices())

    def test_graph_with_duplicates(self):
        graph = DirectedGraph([1, 2, 2], [(1,2), (1,2)])
        self.assertEquals(1, graph.get_number_of_edges())
        self.assertEquals(2, graph.get_number_of_vertices())
        
    def test_get_indegrees_for_graph_with_one_edge(self):
        graph = DirectedGraph([1, 2], [(1,2)])
        self.assertEquals(0, graph.get_indegrees(1))
        self.assertEquals(1, graph.get_indegrees(2))
    
    def test_get_outdegrees_for_graph_with_one_edge(self):
        graph = DirectedGraph([1, 2], [(1,2)])
        self.assertEquals(1, graph.get_outdegrees(1))
        self.assertEquals(0, graph.get_outdegrees(2))

    def test_serialize_deserialize(self):
        original_graph = DirectedGraph([1,2], [(1,2)])
        backup = pickle.dumps(original_graph)
        recovered_graph = pickle.loads(backup)
        self.assertEquals(1, recovered_graph.get_number_of_edges())
        self.assertEquals(2, recovered_graph.get_number_of_vertices())
        self.assertEquals(0, recovered_graph.get_indegrees(1))
        self.assertEquals(1, recovered_graph.get_indegrees(2))
        self.assertEquals(1, recovered_graph.get_outdegrees(1))
        self.assertEquals(0, recovered_graph.get_outdegrees(2))


if __name__ == "__main__":
    unittest.main()