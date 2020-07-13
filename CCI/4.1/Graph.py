class Graph:
    def __init__(self, nodes):
        self.nodes = []
        for node in nodes:
            self.nodes.append(GraphNode(node))

class GraphNode:
    def __init__(self, x):
        self.val = x
        self.children = []
        self.visited = False
