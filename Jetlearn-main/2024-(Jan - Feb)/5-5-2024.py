# Creating a dictionary with graph

Graph = {
    "a" : ["b","c"],
    "b" : ["a","d"],
    "c" : ["a","d"],
    "d" : ["e"],
    "e" : ["d"]
}

print(Graph)

# Display Graph Vertices

class _Graph:
    def __init__(self, GraphDictionary = None | dict):
        if GraphDictionary is None:
            GraphDictionary = []

        self.GraphDictionary = GraphDictionary

    def Edges(self):
        return self.FindEdges()
    
    def FindEdges(self):
        EdgeName = []

        for abc in self.GraphDictionary:
            for next in self.GraphDictionary[abc]:
                if {next, abc} not in EdgeName:
                    EdgeName.append({next, abc})

        return EdgeName

    def GetVertices(self):
        return list(self.GraphDictionary.keys())
    
    def AddVertex(self, Abc):
        if Abc not in self.GraphDictionary:
            self.GraphDictionary[Abc] = []


    
graph_elements = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}

New = _Graph(graph_elements)

New.AddVertex("f")

print(New.GetVertices())

print(New.Edges())