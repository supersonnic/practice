from CCI.LinkedList import LinkedList, Node

# def is_pal(list):


### Tests
linked_list = LinkedList(Node('a'))
linked_list.add_nodes([Node('b'), Node('c'), Node('c'), Node('b'), Node('b')])
print(linked_list)
print(is_pal(linked_list))
print ("\n")
