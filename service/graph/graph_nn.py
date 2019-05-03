N      = 0 # N aka number of node

array1 = [0] * N
A      = array1 * N # N*N matrix representing the graph/node-network

node_names = dict()
node_ids   = dict()

def load(init_data:dict):
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

    global node_names; node_names = dict()
    global node_ids;   node_ids   = dict()
    for i, node_name in enumerate(a):
        node_names[i]       = node_name
        node_ids[node_name] = i
    #endregion

    # load the graph
    global N; N = len(node_names)
    global A; array1 = [0] * N; A = array1*N
    for node_name in init_data:
        i = node_ids[node_name]
        neighbor_node_names = init_data[node_name]
        for nnn in neighbor_node_names:
            j = node_ids[nnn]
            A[i][j] = 1
            A[j][i] = 1
