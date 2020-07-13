from LinkedList import LinkedList, Node

def find_kth(linked_list, k):
    return travel(linked_list.head, 0, 0, k)

def travel(node, count, length, k):
    if not node:
        return
    travel (node.next, count, length + 1, k)
    if length - count == k:
        return count



### Tests
# linked_list = LinkedList(Node(0))
# print(linked_list)
# print(find_kth(linked_list, 1))
# print ("\n")
#
# linked_list = LinkedList(Node(0))
# linked_list.add_nodes([Node(1), Node(2), Node(3), Node(4)])
# print(linked_list)
# print(find_kth(linked_list, -2))
# print ("\n")
#
# linked_list = LinkedList(Node(0))
# linked_list.add_nodes([Node(1), Node(2), Node(3), Node(4)])
# print(linked_list)
# print(find_kth(linked_list, 0))
# print ("\n")
#
# linked_list = LinkedList(Node(0))
# linked_list.add_nodes([Node(1), Node(2), Node(3), Node(4)])
# print(find_kth(linked_list, 1))
# print(linked_list)
# print ("\n")

linked_list = LinkedList(Node(0))
linked_list.add_nodes([Node(1), Node(2), Node(3), Node(4)])
print(find_kth(linked_list, 2))
print(linked_list)
print ("\n")

# linked_list = LinkedList(Node(0))
# linked_list.add_nodes([Node(1), Node(2), Node(3), Node(4)])
# print(find_kth(linked_list, 5))
# print(linked_list)
# print ("\n")
#
# linked_list = LinkedList(Node(0))
# linked_list.add_nodes([Node(1), Node(2), Node(3), Node(4)])
# print(find_kth(linked_list, 6))
# print(linked_list)
# print ("\n")
