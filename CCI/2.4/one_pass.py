# WRONG SOLUTION
from LinkedList import LinkedList, Node

def partition(linked_list, p):
    runner = linked_list.head
    mid = linked_list.head
    if runner.next == None:
        return linked_list
    # while mid.next != None and mid.value >= p:
    #     mid = mid.next
    # if mid.next == None:
    #     return linked_list
    # if mid != runner:
    #     temp = mid
    #     mid = runner
    #     runner = mid
    while runner.next != None:
        if runner.next.value < p:
            temp = runner.next
            runner.next = runner.next.next
            temp.next = mid.next
            mid.next = temp
            mid = mid.next
            continue
        runner = runner.next
    return linked_list

### Tests
linked_list = LinkedList(Node(3))
linked_list.add_nodes([Node(5), Node(8), Node(5), Node(10), Node(2), Node(1)])
print(linked_list)
print(partition(linked_list, 5))
print ("\n")

linked_list = LinkedList(Node(3))
linked_list.add_nodes([Node(5), Node(8), Node(5), Node(10), Node(2), Node(1)])
print(linked_list)
print(partition(linked_list, 8))
print ("\n")
