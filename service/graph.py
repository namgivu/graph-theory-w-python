class Graph:

    G = dict() # G aka graph; { v : {neighbor of v} }
    V = set()  # V aka vertices
    E = list() # E aka edges

    def __init__(self, initial_data:dict):
        self.load(initial_data)


    def load(self, initial_data:dict):
        self.G = {}
        for k in initial_data:
            k_values = initial_data[k]
            self.G[k] = set()
            for v in k_values:
                self.G[k].add(v)

        #region load vertices
        self.V = set()
        for v in self.G:
            self.V.add(v)
            neighbor_v = self.G.get(v)
            self.V.update(neighbor_v) # neighbor_v aka neighbor vertices of :v # add list to a set ref. https://stackoverflow.com/a/43746275/248616
        #endregion

        #region load edges
        self.E = list()
        for v in self.G:
            neighbor_v = self.G.get(v) # neighbor_v aka neighbor vertices of :v
            for nv in neighbor_v:
                e = {v, nv} # e aka edges
                if e not in self.E:
                    self.E.append(e)
        #endregion


    def get_vertices(self):
        return self.V


    def get_edges(self):
        return self.E


    def add_vertex(self, v:'str as new_vertex_name'):
        # update G
        if v not in self.G: self.G[v] = set()

        # update V
        self.V.add(v)

        # update E - no need as ne vertex has no edge yet
        pass


    def add_edges(self, e:'set(v, nv) as new_edge_v_nv'):
        # update V
        v, nv = sorted(e) # v aka vertex, nv aka neighbor of :v
        self.add_vertex(v)
        self.add_vertex(nv)

        # update G
        if self.G.get(v): self.G[v].add(nv)
        else:             self.G[v] = [nv]

        if self.G.get(nv): self.G[nv].add(v)
        else:              self.G[nv] = [v]

        # update E
        self.E.append(e)
