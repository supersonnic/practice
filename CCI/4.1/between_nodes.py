from Graph import Graph, GraphNode

def between_nodes(graph, node1, node2):
    connected = False
    if node1.children:
        connected = search(graph, node1, node2)
    if node2.children:
        connected = search(graph, node2, node1)
    return connected

def search(graph, fromNode, toNode):
    queue = [fromNode]
    while queue:
        node = queue.pop(0)
        # node.visited = True
        if node.val == toNode.val:
            return True
        for child in node.children:
            # if not child.visited:
                queue.append(child)
    return False


graph = Graph([0, 1, 2, 3, 4, 5, 6, 7])
graph.nodes[0].children = [graph.nodes[1], graph.nodes[4]]
graph.nodes[1].children = [graph.nodes[2]]
graph.nodes[2].children = [graph.nodes[7]]
graph.nodes[3].children = [graph.nodes[1], graph.nodes[5]]
graph.nodes[4].children = []
graph.nodes[5].children = [graph.nodes[6], graph.nodes[4]]
graph.nodes[6].children = [graph.nodes[7]]
graph.nodes[7].children = [graph.nodes[2]]
print(between_nodes(graph, graph.nodes[4], graph.nodes[0]))
print(between_nodes(graph, graph.nodes[2], graph.nodes[7]))
