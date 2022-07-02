import unittest

from directedgraph import DirectedGraph

class DirectedGraphTest(unittest.TestCase):

    def test_empty_graph_returns_zero_edges(self):
        graph = DirectedGraph([], [])
        self.assertEqual(0, graph.get_number_of_edges())


if __name__ == "__main__":
    unittest.main()