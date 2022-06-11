from stack_array import *

class vertex:
    def __init__(self, adjacencies: List):
        self.in_degree = 0
        self.adjacencies = adjacencies

def tsort(vertices: List) -> str:
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility {@code tsort}.  That is, one vertex per
    * line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''
    
    # creating adjacency list using dictionary where key is the string name of the vertex 
    # and the value is vertex structure with in_degree and adajacencies

    if len(vertices) == 0:
        raise ValueError("input contains no edges")

    if len(vertices) % 2 != 0:
        raise ValueError("input contains an odd number of tokens")

    adjacency_list: dict = {}
    for i in range(len(vertices)):

        ver = vertices[i]

        if i % 2 == 0 and adjacency_list.get(ver) is None:
            adjacency_list[ver] = vertex([])

        elif i % 2 != 0 and adjacency_list.get(ver) is None:
            adjacency_list[ver] = vertex([])
            adjacency_list[ver].in_degree += 1

            # adding this string to the adjacencies of the index behind it
            adjacency_list[vertices[i-1]].adjacencies.append(ver)

        elif i % 2 != 0 and adjacency_list.get(ver) is not None:
            adjacency_list[ver].in_degree += 1
            
            # adding this string to the adjacencies of the index behind it if it's not there before
            if ver not in adjacency_list[vertices[i-1]].adjacencies:
                adjacency_list[vertices[i-1]].adjacencies.append(ver)
    
    adj_list_stack = Stack(len(list(adjacency_list.keys())))
    output = []

    # looping through the adjacency_list to push into stack 
    for key in adjacency_list.keys():
        if adjacency_list[key].in_degree == 0:
            adj_list_stack.push(key)

    # pop and bop
    while not adj_list_stack.is_empty():
        encountered = adj_list_stack.pop()
        output.append(encountered)
        for ver in adjacency_list[encountered].adjacencies:
            adj_vertices = adjacency_list[ver]
            adj_vertices.in_degree -= 1

            if adj_vertices.in_degree == 0:
                adj_list_stack.push(ver)
    
    # checking for cycles
    if len(adjacency_list.keys()) != len(output):
        raise ValueError("input contains a cycle")

    return "\n".join(output)