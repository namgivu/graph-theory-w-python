class Graph:
    G = dict() # G aka graph
    V = set()  # V aka Vertices of G

    def __init__(self, initial_data:dict):
        self.G = initial_data

        self.V = set()
        for v in self.G:
            self.V.add(v)
            neighbor_v = self.G.get(v); self.V.update(neighbor_v) # add list to a set ref. https://stackoverflow.com/a/43746275/248616


    def get_vertices(self, sort=False):
        return self.V if not sort else sorted(self.V)
