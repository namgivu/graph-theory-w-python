class GraphNN:

    N      = 0 # N aka number of node
    A      = [[0 for __ in range(N)] for _ in range(N)] # N*N matrix representing the graph/node-network
    G      = {'some-node': {'neighbor0', 'neighbor1', 'neighbor2'}}

    node_names = dict()
    node_ids   = dict()


    def load(self, init_data:dict):
        """
        *sample input*
        {
            # node_name: [ neighbor_nodes]
            'a': ['d'],
            'b': ['c'],
            'c': ['b', 'c', 'd', 'e'],
            'd': ['a', 'c'],
            'e': ['c'],
            'f': [],
        }
        """

        #region collect node names
        s = set() # s aka set
        for node_name in init_data: # node => node's neighbor
            s.add(node_name)
            neighbor_node_names = init_data[node_name]
            s.update(neighbor_node_names)
        a = sorted(s) # a aka array

        self.node_names = dict()
        self.node_ids   = dict()
        for i, node_name in enumerate(a):
            self.node_names[i]       = node_name
            self.node_ids[node_name] = i
        #endregion

        # load the graph as A[i,j]
        N = len(self.node_names)
        self.A = [[0 for __ in range(N)] for _ in range(N)]
        for node_name in init_data:
            i = self.node_ids[node_name]
            neighbor_node_names = init_data[node_name]
            for nnn in neighbor_node_names:
                j = self.node_ids[nnn]
                self.A[i][j] = 1
                self.A[j][i] = 1

        # load the graph as G{ node -> neighbor_set }
        self.G = dict()
        for node_name in init_data:
            i = self.node_ids[node_name]
            self.G[i] = set()

            neighbor_node_names = init_data[node_name]
            for nnn in neighbor_node_names:
                j = self.node_ids[nnn]
                self.G[i].add(j)


    def find_path(self, from_node_name, to_node_name):
        if from_node_name not in self.node_ids.keys(): return []
        if to_node_name   not in self.node_ids.keys(): return []

        node_f = self.node_ids[from_node_name] # node_f aka from node
        node_t = self.node_ids[to_node_name]   # node_t aka to node aka target node

        s1 = set(); s1.add(node_f)
        s2 = set()
        tr = {}; tr[node_f]=None # tr aka trace back; tr[i] == node before node :i
        while len(s1)>0:
            #region find nodes connected with s1, save to s2
            for i in s1:
                #region find nodes j connected to i
                for j in self.G[i]:
                    if tr.get(j) is None:
                        tr[j] = i
                        s2.add(j)
                #endregion
            #endregion

            if tr.get(node_t): break # we found the target node, seek no more

            # continue with nodes found in s2
            s1 = s2
            s2 = set()

        if tr.get(node_t) is None: return [] # we cannot reach the target node

        p = [] # p aka path
        i = node_t
        while i!=node_f:
            p.append(i)
            i = tr[i]
        p.append(i)

        p = p[::-1]
        return p
