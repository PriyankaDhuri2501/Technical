class AdjacencyMatrix:
    def __init__(self,num_vertices):
        self.num_vertices = num_vertices
        self.vertices = [None] * num_vertices
        self.adj_matrix = [ [0] * num_vertices for row in range(num_vertices)]

    def add_vertex(self,index,label):
        if(index >=0 and index<self.num_vertices):
            self.vertices[index] = label
        else:
            print(f"Matrix of {index}")

    def add_edge(self,source,destination,weight = 1):
        if (0 <= source < self.num_vertices and 0<= destination < self.num_vertices):
            self.adj_matrix[source][destination] = weight
            self.adj_matrix[destination][source] = weight

    def display(self):
        for index,label in enumerate(self.vertices):
            if label != None:
                print(f,"Vertex Index : {index}, label : {label}")
        for row in self.adj_matrix:
            print(row)

        
g = AdjacencyMatrix(4)
g.add_vertex(0,'A')
g.add_vertex(1,'B')
g.add_vertex(2,'C')

g.add_edge("A","B",4)
g.add_edge("B","C",6)
g.add_edges("A","C",5)

g.display()

# no. of unreachable nodes
# eventual safe states
# count element on subtrees
# no. of complete components
# centre of star graph
# all paths from source to target
# keys and rooms
# no. of provisions
