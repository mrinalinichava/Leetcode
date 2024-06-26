# class Vertex:
#     def __init__(self,vertexId):
#         self.id = vertexId
#         self.neighbours = []
#
#     def addneighbour(self,neighbour):
#         for neighbour in self.neighbours:
#             self.neighbours.append(neighbour)
#
#
# class Graph:
#     def __init__(self):
#         self.vertices = {}
#
#     def addvertex(self,vertex):
#         pass



class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        for key,val in edges:
            if key in self.graph_dict:
                self.graph_dict[key].append(val)
            else:
                self.graph_dict[key] = [val]
        print("Graph Dict : ", self.graph_dict)

    def getPaths(self,start,end,path=[]):
        path = path +[start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for place in self.graph_dict[start]:
            if(place not in path):
                new_paths = self.getPaths(place,end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def getShortestPath(self,start,end):
        return self.getshortest(start, end, [])

    def getshortest(self,start, end, path):
        path = path + [start]
        if (start == end):
            return path
        if start not in self.graph_dict:
            return None
        shortest_path = None
        for place in self.graph_dict[start]:
            if(place not in path):
                sp = self.getshortest(place,end,path)
                if sp:
                    if shortest_path is None:
                        shortest_path = sp
                    if shortest_path is None or len(sp)<len(shortest_path):
                        shortest_path=sp

                # shortest_path = min(shortest_path,sp)
        return shortest_path




if __name__ == '__main__':
    routes = [("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","NY"),("Dubai","NY"),("NY","TORONTO")]
    route_graph = Graph(routes)
    print(route_graph.getPaths("Mumbai","NY",[]))
    start = "Mumbai"
    end = "NY"
    print(f"shortest path between {start} and {end} :", route_graph.getShortestPath(start,end))




