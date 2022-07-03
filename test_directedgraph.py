import unittest
import pickle

from directedgraph import DirectedGraph

class DirectedGraphTest(unittest.TestCase):

    def test_empty_graph_returns_zero_edges(self):
        graph = DirectedGraph([], [])
        self.assertEqual(0, graph.get_number_of_edges())

    def test_graph_with_one_edge(self):
        graph = DirectedGraph([1, 2], [(1,2)])
        self.assertEqual(1, graph.get_number_of_edges())
        self.assertEqual(2, graph.get_number_of_vertices())

    def test_graph_with_duplicates(self):
        graph = DirectedGraph([1, 2, 2], [(1,2), (1,2)])
        self.assertEqual(1, graph.get_number_of_edges())
        self.assertEqual(2, graph.get_number_of_vertices())

    def test_get_indegrees_for_graph_with_one_edge(self):
        graph = DirectedGraph([1, 2], [(1,2)])
        self.assertEqual(0, graph.get_indegrees(1))
        self.assertEqual(1, graph.get_indegrees(2))

    def test_get_outdegrees_for_graph_with_one_edge(self):
        graph = DirectedGraph([1, 2], [(1,2)])
        self.assertEqual(1, graph.get_outdegrees(1))
        self.assertEqual(0, graph.get_outdegrees(2))

    def test_cannot_create_edge_if_no_vertex_exists(self):
        with self.assertRaises(ValueError):
            DirectedGraph([], [(0,1)])

    def test_cannot_create_edge_to_same_vertex(self):
        with self.assertRaises(ValueError):
            DirectedGraph([1], [(1,1)])

    def test_serialize_deserialize(self):
        original_graph = DirectedGraph([1,2], [(1,2)])
        backup = pickle.dumps(original_graph)
        recovered_graph = pickle.loads(backup)
        self.assertEqual(1, recovered_graph.get_number_of_edges())
        self.assertEqual(2, recovered_graph.get_number_of_vertices())
        self.assertEqual(0, recovered_graph.get_indegrees(1))
        self.assertEqual(1, recovered_graph.get_indegrees(2))
        self.assertEqual(1, recovered_graph.get_outdegrees(1))
        self.assertEqual(0, recovered_graph.get_outdegrees(2))


if __name__ == "__main__":
    unittest.main()
