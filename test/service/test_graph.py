import unittest

from service.graph import Graph


class Test(unittest.TestCase):

    def test(self):
        """ref. https://www.python-course.eu/graphs_python.php"""
        d = {
            'a': ['d'],
            'b': ['c'],
            'c': ['b', 'c', 'd', 'e'],
            'd': ['a', 'c'],
            'e': ['c'],
            'f': [],
        }
        g = Graph(d)
        vertices=g.get_vertices();          print(f'\nVertices: {vertices}')
        vertices=g.get_vertices(sort=True); print(  f'          {vertices}')

        edges=g.get_edges(); print(f'\nEdges: {edges}')
