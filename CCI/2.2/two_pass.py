from LinkedList import LinkedList, Node

def find_kth(linked_list, k):
    if k <= 0:
        return None
    current = linked_list.head
    length = 1
    while current.next != None:
        length += 1
        current = current.next
    kth = length - k
    if kth < 0:
        return None
    current = linked_list.head
    while kth > 0:
        current = current.next
        kth -= 1
    return current.value

### Tests
linked_list = LinkedList(Node(0))
print(linked_list)
print(find_kth(linked_list, 1))
print ("\n")

linked_list = LinkedList(Node(0))
linked_list.add_nodes([Node(1), Node(2), Node(3), Node(4)])
print(linked_list)
print(find_kth(linked_list, -2))
print ("\n")

linked_list = LinkedList(Node(0))
linked_list.add_nodes([Node(1), Node(2), Node(3), Node(4)])
print(linked_list)
print(find_kth(linked_list, 0))
print ("\n")

linked_list = LinkedList(Node(0))
linked_list.add_nodes([Node(1), Node(2), Node(3), Node(4)])
print(find_kth(linked_list, 1))
print(linked_list)
print ("\n")

linked_list = LinkedList(Node(0))
linked_list.add_nodes([Node(1), Node(2), Node(3), Node(4)])
print(find_kth(linked_list, 2))
print(linked_list)
print ("\n")

linked_list = LinkedList(Node(0))
linked_list.add_nodes([Node(1), Node(2), Node(3), Node(4)])
print(find_kth(linked_list, 5))
print(linked_list)
print ("\n")

linked_list = LinkedList(Node(0))
linked_list.add_nodes([Node(1), Node(2), Node(3), Node(4)])
print(find_kth(linked_list, 6))
print(linked_list)
print ("\n")
