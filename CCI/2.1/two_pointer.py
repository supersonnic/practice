from LinkedList import LinkedList, Node

def remove_dups(l):
    if not l:
        return l
    p1 = l.head
    while p1:
        p2 = p1
        while p2 and p2.next:
            while p2.next and (p1.value == p2.next.value):
                p2.next = p2.next.next
            p2 = p2.next
        p1 = p1.next
    return l

### Tests
linked_list = LinkedList(Node(0))
print(linked_list)
remove_dups(linked_list)
print(linked_list)
print ("\n")

linked_list = LinkedList(Node(0))
linked_list.add_nodes([Node(0), Node(1), Node(2), Node(3)])
print(linked_list)
remove_dups(linked_list)
print(linked_list)
print ("\n")

linked_list = LinkedList(Node(0))
linked_list.add_nodes([Node(1), Node(2), Node(2), Node(3)])
print(linked_list)
remove_dups(linked_list)
print(linked_list)
print ("\n")

linked_list = LinkedList(Node(0))
linked_list.add_nodes([Node(1), Node(2), Node(3), Node(3)])
print(linked_list)
remove_dups(linked_list)
print(linked_list)
print ("\n")

linked_list = LinkedList(Node(0))
linked_list.add_nodes([Node(1), Node(2), Node(3), Node(0)])
print(linked_list)
remove_dups(linked_list)
print(linked_list)
print ("\n")

linked_list = LinkedList(Node(0))
linked_list.add_nodes([Node(1), Node(2), Node(1), Node(4)])
print(linked_list)
remove_dups(linked_list)
print(linked_list)
print ("\n")
