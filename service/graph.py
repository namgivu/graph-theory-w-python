class Graph:

    G = dict() # G aka graph
    V = set()  # V aka vertices
    E = list() # E aka edges

    def __init__(self, initial_data:dict):
        self.G = initial_data

        #region load vertices
        self.V = set()
        for v in self.G:
            self.V.add(v)
            neighbor_v = self.G.get(v); self.V.update(neighbor_v) # neighbor_v aka neighbor vertices of :v # add list to a set ref. https://stackoverflow.com/a/43746275/248616
        #endregion

        #region load edges
        self.E = list()
        for v in self.G:
            neighbor_v = self.G.get(v) # neighbor_v aka neighbor vertices of :v
            for nv in neighbor_v:
                e = {v, nv}; e = sorted(e) # e aka edges
                if e not in self.E:
                    self.E.append(e)
        #endregion


    def get_vertices(self, sort=False):
        return self.V if not sort else sorted(self.V)


    def get_edges(self):
        return self.E
