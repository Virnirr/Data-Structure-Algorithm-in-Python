from typing import Any, List, Optional
from stack_array import * # Needed for Depth First Search
from queue_array import * # Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key: Any):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to: List = []
        self.visited = False
        self.color = None

class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename: str):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        
        # dictionary for creating key as the vertex and value as Vertex() instantiation
        self.adj_list: dict = {}

        with open(filename, "rt") as file:

            # look through each of the file and split the vertex into a list. 
            # add lines[0] and lines[1] adj_list as two undirected vertices with each other as adjacency to each other.
            # all will be stored in self.adj_list with key, value pair where key is the vertex and the value the Vertex() instantiation
            for lines in file:
                ver = lines.split()
                if self.adj_list.get(ver[0]) is None:
                    self.adj_list[ver[0]] = Vertex(ver[0])
                    if ver[1] not in self.adj_list[ver[0]].adjacent_to:
                        self.adj_list[ver[0]].adjacent_to.append(ver[1])
                
                else:
                    if ver[1] not in self.adj_list[ver[0]].adjacent_to:
                        self.adj_list[ver[0]].adjacent_to.append(ver[1])
                
                if self.adj_list.get(ver[1]) is None:
                    self.adj_list[ver[1]] = Vertex(ver[1])
                    if ver[0] not in self.adj_list[ver[1]].adjacent_to:
                        self.adj_list[ver[1]].adjacent_to.append(ver[0])
                
                else:
                    if ver[0] not in self.adj_list[ver[1]].adjacent_to:
                        self.adj_list[ver[1]].adjacent_to.append(ver[0])

    def add_vertex(self, key: Any) -> None:
        '''Add vertex to graph, only if the vertex is not already in the graph.'''

        if self.adj_list.get(key) is None:
            self.adj_list[key] = Vertex(key)

    def get_vertex(self, key: Any) -> Optional[Vertex]:
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        if self.adj_list.get(key) is not None:
            return self.adj_list[key]
        
        return None

    def add_edge(self, v1: Any, v2: Any) -> None:
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''

        # check if they are already in the adjacency or not
        if v2 not in self.adj_list[v1].adjacent_to:
            self.adj_list[v1].adjacent_to.append(v2)

        if v1 not in self.adj_list[v2].adjacent_to:
            self.adj_list[v2].adjacent_to.append(v1)

    def get_vertices(self) -> List:
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''

        vertex_list_id = list(self.adj_list.keys())
        vertex_list_id.sort()

        return vertex_list_id

    def conn_components(self) -> List:
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        
        adj_list_stack = Stack(len(list(self.adj_list.keys())))

        list_of_connections = []

        # loop through whole list by when it was inserted
        for vertex in self.adj_list.keys():
            connections = []    

            # check if the key is visited or not
            if not self.adj_list[vertex].visited:
                adj_list_stack.push(vertex) # push the vertex we're checking to stack
                # do depth first search algorithm
                # check if the stack is empty or not and pop() if it isn't
                # add the adjacenct list of the popped vertex onto the stack 
                # make the popped vertex visited as True so you don't add it into the stack again
                while not adj_list_stack.is_empty():
                    ver = adj_list_stack.pop()
                    if not self.adj_list[ver].visited:
                        connections.append(ver)
                        self.adj_list[ver].visited = True

                    # start from the back of the adjacency list and loop through
                    for adj in self.adj_list[ver].adjacent_to[::-1]:
                        if not self.adj_list[adj].visited:
                            adj_list_stack.push(adj)
                
                connections.sort()
                list_of_connections.append(connections)
        
        return list_of_connections

    def is_bipartite(self) -> bool:
        '''Returns True if the graph is bicolorable and False otherwise.
        This method MUST use Breadth First Search logic!'''
        
        adj_list_queue = Queue(len(list(self.adj_list.keys())))

        for ver in self.get_vertices():
                
            if self.adj_list[ver].color is None:
                self.adj_list[ver].color = "Red"
                adj_list_queue.enqueue(ver)
                while not adj_list_queue.is_empty():
                    encounter = self.adj_list[adj_list_queue.dequeue()]
                    for adj_ver in encounter.adjacent_to:
                        if encounter.color == "Red" and self.adj_list[adj_ver].color is None:
                            self.adj_list[adj_ver].color = "Blue"
                            adj_list_queue.enqueue(adj_ver)
                        
                        elif encounter.color == "Blue" and self.adj_list[adj_ver].color is None:
                            self.adj_list[adj_ver].color = "Red"
                            adj_list_queue.enqueue(adj_ver)

                        elif encounter.color == self.adj_list[adj_ver].color:
                            return False

        return True