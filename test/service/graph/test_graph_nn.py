import unittest
import service.graph.graph_nn as GraphNN; G = GraphNN # G defined as short alias


class Test(unittest.TestCase):

    def test(self):
        d = {
            'a': ['d'],
            'b': ['c'],
            'c': ['b', 'c', 'd', 'e'],
            'd': ['a', 'c'],
            'e': ['c'],
            'f': [],
        }
        G.load(d)
        assert set(G.node_names.keys()  ) == { 0,   1,   2,   3,   4,   5,  }
        assert set(G.node_names.values()) == {'a', 'b', 'c', 'd', 'e', 'f', }
