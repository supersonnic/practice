### Node definition
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

### LinkedList definition
class LinkedList:
    def __init__(self, head_node):
        self.head = head_node

    def add_node(self, node):
        current = self.head
        while True:
            if current.next == None:
                current.next = node
                break
            current = current.next

    def add_nodes(self, nodes):
        current = self.head
        while True:
            if current.next == None:
                for node in nodes:
                    current.next = node
                    current = current.next
                break
            current = current.next

    def remove_node(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
            return True
        while True:
            if current.next == None:
                return False
            if current.next.value == value:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def __repr__(self):
        nodes = []
        current = self.head
        while True:
            nodes.append(current.value)
            if current.next == None:
                break
            current = current.next
        return (str(nodes))

### Tests
# linked_list = LinkedList(Node(0))
# for i in range(1, 21):
#     node = Node(i)
#     linked_list.add_node(node)
# print(linked_list)
# linked_list.remove_node(20)
# print(linked_list)
# linked_list.add_nodes([Node(0),Node(0),Node(0)])
# print(linked_list)
