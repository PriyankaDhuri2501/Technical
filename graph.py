class GraphEdgeList:
    def __init__(self):
        self.v = []
        self.edges = []

    def add_vertex(self,vertex):
        if(vertex not in self.v):
            self.v.append(vertex)
        else:
            print(f"{vertex} already exists")
        return
    
    def add_edge(self,source,destination,weight = 1):
        if source in self.v and destination in self.v:
            edge = (source,destination,weight)
            self.edges.append(edge)
        else:
            print("One or both the vertices are not found")

    def display(self):
        print("Vertices:")
        for vertex in self.v:
            print(f"Vertex: {vertex}")
        for source,destination,weight in self.edges:
            print(f"{source} ---> {destination} and weight is{weight}")


graph = GraphEdgeList()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)

graph.add_edge(1,2)
graph.add_edge(2,3)

graph.display()