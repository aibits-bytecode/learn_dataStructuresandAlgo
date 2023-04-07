class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_paths(node,end,path)
                for p in new_path:
                    paths.append(p)
        return paths

    def get_shortest_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []

        shortest_paths = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_paths(node,end,path)
                if sp:
                    if shortest_paths is None or len(sp)<len(shortest_paths):
                        shortest_paths = sp
        return shortest_paths





    def print(self):
        print(self.graph_dict)


if __name__ == "__main__":
    routes = [
        ("mumbai", "paris"),
        ("mumbai", "dubai"),
        ("paris", "dubai"),
        ("paris", "new york"),
        ("dubai", "new york"),
        ("new york", "toronto")
    ]

    graph = Graph(routes)
    graph.print()
    print(graph.get_shortest_paths("mumbai", "toronto"))