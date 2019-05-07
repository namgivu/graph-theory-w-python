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
        a = { from_n }
        b = set()
        tr = { from_n: -1} # tr aka trace back
        while len(a)>0:
            for i in a: # spread from :a, store connected nodes in :b
                for j in self.A[i].keys():
                    if tr.get(j) is None:
                        tr[j] = i
                        b.add(j)
            if tr.get(to_n): break # we found :to_n, no need to seek more

            # seek next
            a=b; b=set()

        if tr.get(to_n) is None: return None # path not found

        # found a path --> build path from :tr
        i = to_n
        path = []
        while i!=-1:
            path.append(i)
            i = tr.get(i)
        path = path[::-1] # reverse :path
        return path


    def get_trees(self):
        """ trees aka isolated-regions"""
        pass


    def get_shortest_paths(self, from_n, to_n):
        pass
