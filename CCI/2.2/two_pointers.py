from LinkedList import LinkedList, Node

def find_kth(linked_list, k):
    if k <= 0:
        return None
    end_pointer = linked_list.head
    k_pointer = linked_list.head
    count = 1
    while end_pointer.next != None:
        if count >= k:
            k_pointer = k_pointer.next
        count += 1
        end_pointer = end_pointer.next
    if k > count:
        return None
    return k_pointer.value

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
