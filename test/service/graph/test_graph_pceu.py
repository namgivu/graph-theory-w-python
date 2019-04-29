import unittest
from service.graph.graph_pceu import GraphPCEU


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

        # load graph
        g = GraphPCEU(d)
        assert g.G.keys() == d.keys()
        for v in g.G.keys():
            assert set(g.G.get(v)) == set(d.get(v))

        assert g.V == {'a', 'b', 'c', 'd', 'e', 'f'}

        assert len(g.E) == 5
        assert {'a', 'd'} in g.E
        assert {'b', 'c'} in g.E
        assert {'c', 'c'} in g.E
        assert {'c', 'd'} in g.E
        assert {'c', 'e'} in g.E

        # add vertex
        g = GraphPCEU(d)
        v = 'z'; g.add_vertex(v)
        assert g.G.get('z') == set()
        assert 'z' in g.V

        # add edge
        g = GraphPCEU(d)
        e = {'a','z'}; g.add_edges(e)
        assert 'z' in g.G.get('a'); assert g.G.get('z') == ['a']
        assert 'z' in g.V and 'a' in g.V
        assert e in g.E
