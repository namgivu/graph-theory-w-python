import unittest
from service.graph.graph_nn import GraphNN

GRAPH_FIXTURE = {
    'a': ['d'],
    'b': ['c'],
    'c': ['b', 'c', 'd', 'e'],
    'd': ['a', 'c'],
    'e': ['c'],
    'f': [],
}

GRAPH_FIXTURE2 = {
    'a': ['c'],
    'b': ['c'],
    'c': ['a', 'b', 'd'],
    'd': ['c'],
    'e': ['f'],
    'f': ['e'],
}


class Test(unittest.TestCase):

    def test_load_abcdef(self):
        G = GraphNN()
        G.load(init_data=GRAPH_FIXTURE)
        assert set(G.node_names.keys()  ) == { 0,   1,   2,   3,   4,   5,  }
        assert set(G.node_names.values()) == {'a', 'b', 'c', 'd', 'e', 'f', }


    def test_load_012345(self):
        G = GraphNN()
        d = {
            0 : [3],
            1 : [2],
            2 : [1, 2, 3, 4],
            3 : [0, 2],
            4 : [2],
            5 : [],
        }
        G.load(d)
        assert set(G.node_names.keys()  ) == { 0,   1,   2,   3,   4,   5, }
        assert set(G.node_names.values()) == { 0,   1,   2,   3,   4,   5, }


    def test_find_path(self):
        G = GraphNN()
        G.load(init_data=GRAPH_FIXTURE)
        f='a'; t='b'; ep=['a', 'd', 'c', 'b']; p = G.find_path(f, t); p = [G.node_names[i] for i in p]; assert p == ep
        f='a'; t='f'; ep=[];                   p = G.find_path(f, t); p = [G.node_names[i] for i in p]; assert p == ep
        f='c'; t='c'; ep=['c'];                p = G.find_path(f, t); p = [G.node_names[i] for i in p]; assert p == ep
        f='a'; t='a'; ep=['a'];                p = G.find_path(f, t); p = [G.node_names[i] for i in p]; assert p == ep


    def test_get_trees(self):
        G = GraphNN()
        G.load(init_data=GRAPH_FIXTURE);  t = G.get_trees(); assert t == [0, 0, 0, 0, 0, 1]
        G.load(init_data=GRAPH_FIXTURE2); t = G.get_trees(); assert t == [0, 0, 0, 0, 1, 1]
