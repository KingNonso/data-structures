class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []


class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)  # creates a new node
        self.nodes.append(new_node)  # adds newly created node to nodes array

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        edges = []
        for edge in self.edges:
            e = (edge.value, edge.node_from.value, edge.node_to.value)
            if e in edges:
                pass
            else:
                edges.append(e)
        return edges

    def find_max_index(self):
        max_index = -1
        if len(self.nodes):
            for node in self.nodes:
                if node.value > max_index:
                    max_index = node.value
        return max_index


    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indicies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        adjacent = []

        for r in range(0, len(self.edges)):
            d = self.edges[r]
            print(r, d)
            if r == d.node_from.value:
                f = [(a.node_to.value, a.value) for a in d.node_from.edges]
            else:
                f = None

            adjacent.append(f)

        return adjacent

    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""

        matrix = []

        for r in range(0, len(self.edges)):
            d = self.edges[r]
            if r == d.node_from.value:
                f = [0, 0, 0, 0, 0]
                for a in d.node_from.edges:
                    f[a.node_to.value] = a.value
            else:
                f = [0, 0, 0, 0, 0]
            matrix.append(f)
        return matrix


