import textwrap
import unittest
from service.graph.graph_n import GraphN


F1 = """
a b c d e f
a d
b c
c b d e
d a c
e c
""".strip()


def load_fixture(g, f):
    """
    load graph :g from fixture :f
    """
    lines = f.split('\n')

    g.load_names(names=lines[0].split(' '))

    g.A = {}
    for ii in range(1, len(lines)):
        l = lines[ii].split(' ')

        n = l[0]; neighbors_n = l[1:]
        i = g.get_node_index(n); g.A[i] = {}
        for nn in neighbors_n:
            j = g.get_node_index(nn)
            g.A[i][j] = 1
        abb=122


class Test(unittest.TestCase):

    def test_fixture(self):
        g = GraphN()
        load_fixture(g, F1)
        assert g.N == 6
        assert g.s_to_i == {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5}
        assert g.A.get(0)
        assert g.A[0].get(1) is None
        assert g.A[0][3] == 1


    def test_find_path(self):
        g = GraphN()
        load_fixture(g, F1)

        p=g.find_path(0,1); assert p==[0,3,2,1]
        p=g.find_path(0,2); assert p==[0,3,2]
        p=g.find_path(0,3); assert p==[0,3]
        p=g.find_path(0,4); assert p==[0,3,2,4]
        p=g.find_path(0,5); assert p==None
