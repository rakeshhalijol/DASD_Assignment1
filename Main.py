"""
***********Graph Class Description***********

- Here graph is created based on Adjacency matrix form.

- Graph class contains 3 instance variables. they are,
        - node_count : is a integer which counts total no of nodes in the graph.
        - vertex     : is a list which stores nodes of the graph.
        - graph      : is a 2D list used to store the Adjacency matrix.

- Graph class contains 3 methods they are,
        - __add_node() : is a private method which helps to add a new node to the graph.
        - add_edge()   : is a public method which helps to create a edge between 2 nodes.
        - dfs()        : is a public method which helps to traverse the graph
"""


class Graph:
    def __init__(self):
        self.node_count = 0
        self.vertex = []
        self.graph = []

    def __add_node(self, v):
        if v in self.vertex:
            print("Node already exists")

        else:
            self.node_count += 1
            self.vertex.append(v)
            for row in self.graph:
                row.append(0)
            self.graph.append([0 for _ in range(self.node_count)])

    def add_edge(self, v1, v2):
        if v1 not in self.vertex:
            self.__add_node(v1)
        if v2 not in self.vertex:
            self.__add_node(v2)
        if v1 and v2 in self.vertex:
            index_v1, index_v2 = self.vertex.index(v1), self.vertex.index(v2)
            self.graph[index_v1][index_v2], self.graph[index_v2][index_v1] = 1, 1

    def dfs(self, node):
        visited = list()
        if node not in self.vertex:
            print("Node doesn't exists")
        else:
            stack = [node, ]
            while stack:
                curr = stack.pop()
                if curr not in visited:
                    visited.append(curr)
                    for i, num in enumerate(self.graph[self.vertex.index(curr)]):
                        if num == 1:
                            stack.append(self.vertex[i])
        return visited

    def display(self):
        print(self.vertex)
        for row in self.graph:
            print(row)


def group(g):
    visited = list()
    groups = []
    for node in g.vertex:
        if node not in visited:
            visited = g.dfs(node)
            groups.append(list(visited))
    return groups


g = Graph()
# Input
with open("inputPS06.txt") as file:
    content = file.readlines()
    content = [line.rstrip() for line in content]
for line in content:
    names = line.split("/")
    g.add_edge(names[0], names[1])
file.close()
# Output
with open("outputPS06.txt", "w") as file:
    for i, grp in enumerate(group(g)):
        data = f"Group{i + 1} : There are {len(grp)} participants in the group and they are "
        for name in grp:
            data += name + ","
        file.write(data.rstrip(",") + "\n")
file.close()
