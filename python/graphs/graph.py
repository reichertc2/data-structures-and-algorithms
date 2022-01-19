class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self,value):

        return Vertex(value)


    def add_edge(self,start_edge,end_edge,weight=0):
        pass

    def get_nodes(self):
        return list(self.adjacency_list)

    def get_neighbors(self,vertex):
        pass

    def size(self):
        return len(self.adjacency_list)


# Vertex is a Node
class Vertex:
    def __init__(self,value):
        self.value = value


class Edge:
    pass
