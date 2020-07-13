from LinkedList import LinkedList, Node

def remove_dups(linked_list):
    values = set({})
    current = linked_list.head
    values.add(current.value)
    if current.next == None:
        return linked_list
    while True:
        if current.next.value in values:
            current.next = current.next.next
            if current.next == None:
                break
            else:
                continue
        values.add(current.next.value)
        if current.next.next == None:
            break
        current = current.next
    return linked_list

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
