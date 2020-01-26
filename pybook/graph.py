"""Graphs
A graph is a set of vertices and edges that form connections between the vertices. In a more
formal approach, a graph G is an ordered pair of a set V of vertices and a set E of edges
given as G = (V, E) in formal mathematical notation.
"""
#  Adjacency list
graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['E', 'A']
graph['C'] = ['A', 'B', 'E', 'F']
graph['E'] = ['B', 'C']
graph['F'] = ['C']

print(graph)

#  Adjacency matrix
matrix_elements = sorted(graph.keys())
cols = rows = len(matrix_elements)
adjacency_matrix = [[0 for x in range(rows)] for y in range(cols)]
edges_list = []

for key in matrix_elements:
    for neighbor in graph[key]:
        edges_list.append((key, neighbor))
print(edges_list)  #tuples that form the edges of in the graph
"""  fill our multidimensional array by using 1 to mark the
presence of an edge with the line """

for edge in edges_list:
    index_of_first_vertex = matrix_elements.index(edge[0])
    index_of_second_vertex = matrix_elements.index(edge[1])
    adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1
print(adjacency_matrix)

""" Graph traversal: Breadth-first search
To traverse this graph breadth first, we will employ the use of a queue. The
algorithm creates a list to store the nodes that have been visited as the traversal process
proceeds"""
from collections import deque

def breadth_firth_search(graph, root):
    visited_vertices = list()
    graph_queue = deque([root])
    visited_vertices.append(root)
    node = root

    while len(graph_queue) > 0:
        node = graph_queue.popleft()
        adj_nodes = graph[node]
        remaining_elements = set(adj_nodes).difference(set(visited_vertices))
        print(node, adj_nodes, remaining_elements)

        if len(remaining_elements) > 0:
            for elem in sorted(remaining_elements):
                visited_vertices.append(elem)
                graph_queue.append(elem)
    return visited_vertices


graph = dict()
graph['A'] = ['B', 'G', 'D']
graph['B'] = ['A', 'F', 'E']
graph['C'] = ['F', 'H']
graph['D'] = ['F', 'A']
graph['E'] = ['B', 'G']
graph['F'] = ['B', 'D', 'C']
graph['G'] = ['A', 'E']
graph['H'] = ['C']
breadth_firth_search(graph, 'A')

"""Depth-first search
this algorithm traverses the depth of any particular path in the graph
before traversing its breadth. As such, child nodes are visited first before sibling nodes. It
works on finite graphs and requires the use of a stack to maintain the state of the algorithm:"""

def depth_first_search(graph, root):
    visited_vertices = list()
    graph_stack = list()
    print('###  DEPTH FIRST  ##########')
    graph_stack.append(root)
    node = root
    while len(graph_stack) > 0:
        if node not in visited_vertices:
            visited_vertices.append(node)
        adj_nodes = graph[node]
        print(node, adj_nodes, graph_stack, visited_vertices)
        if set(adj_nodes).issubset(set(visited_vertices)):
            graph_stack.pop()
            if len(graph_stack) > 0:
                node = graph_stack[-1]
            continue
        else:
            remaining_elements = set(adj_nodes).difference(set(visited_vertices))

            first_adj_node = sorted(remaining_elements)[0]
            graph_stack.append(first_adj_node)
            node = first_adj_node
    return visited_vertices


graph = dict()
graph['A'] = ['B', 'S']
graph['B'] = ['A']
graph['S'] = ['A', 'G', 'C']
graph['D'] = ['C']
graph['G'] = ['S', 'F', 'H']
graph['H'] = ['G', 'E']
graph['E'] = ['C', 'H']
graph['F'] = ['C', 'G']
graph['C'] = ['D', 'S', 'E', 'F']

print('final', depth_first_search(graph, 'A'))

