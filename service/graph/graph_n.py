import sys


class GraphN:

    N = 0 # N aka number of node
    A = {
        #    0,1 = 1  0,2 = 22
        0: {   1: 1,    2: 22}
    }

    #region node name
    i_to_s = {'a',       'b'     }
    s_to_i = {'a' : 0,   'b' : 1 }

    def load_names(self, names:list):
        self.N      = len(names)
        self.i_to_s = names
        self.s_to_i = { name:i for i,name in enumerate(names) }

    def get_node_name(self, at_index:int):
        return self.i_to_s[at_index]

    def get_node_index(self, node_name:str):
        return self.s_to_i[node_name]
    #endregion




    def find_path(self, from_n, to_n):
        pass


    def get_trees(self):
        """ trees aka isolated-regions"""
        pass


    def get_shortest_paths(self, from_n, to_n):
        pass
