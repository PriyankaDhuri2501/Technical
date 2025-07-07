class GraphAdjacencyList:
    def __init__(self):
        self.V = []
        self.adj_List = {}

    def add_vertex(self,vertex):
        if vertex not in self.V:
            self.V.append(vertex)
            self.adj_List[vertex] =[]

        else:
            print(f"Vertex {vertex} already exists")

    def add_edges(self,source,destination,weight = 1):
        if source in self.V and destination in self.V:
            self.adj_List[source].append((destination,weight))
            self.adj_List[destination].append((source,weight))
        else:
            print("One or both the vertices are not found")

    def display(self):

        for vertex,neighbor in self.adj_List.items():
            print(f"{vertex} : {neighbor}")

graph = GraphAdjacencyList()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")


graph.add_edges("A","B",4)
graph.add_edges("B","C",6)
graph.add_edges("A","C",5)

graph.display()