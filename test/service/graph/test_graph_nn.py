import unittest
import service.graph.graph_nn as GraphNN; G = GraphNN # G defined as short alias

GRAPH_FIXTURE = {
    'a': ['d'],
    'b': ['c'],
    'c': ['b', 'c', 'd', 'e'],
    'd': ['a', 'c'],
    'e': ['c'],
    'f': [],
}


class Test(unittest.TestCase):

    def test_load_abcdef(self):
        G.load(init_data=GRAPH_FIXTURE)
        assert set(G.node_names.keys()  ) == { 0,   1,   2,   3,   4,   5,  }
        assert set(G.node_names.values()) == {'a', 'b', 'c', 'd', 'e', 'f', }


    def test_load_012345(self):
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
        G.load(init_data=GRAPH_FIXTURE)
        # f='a'; t='b'; ep=['a', 'd', 'c', 'b']; p = G.find_path(f, t); p = [G.node_names[i] for i in p]; assert p == ep
        # f='a'; t='f'; ep=[];                   p = G.find_path(f, t); p = [G.node_names[i] for i in p]; assert p == ep
        # f='c'; t='c'; ep=['c'];                p = G.find_path(f, t); p = [G.node_names[i] for i in p]; assert p == ep
        f='a'; t='a'; ep=['a'];                p = G.find_path(f, t); p = [G.node_names[i] for i in p]; assert p == ep
