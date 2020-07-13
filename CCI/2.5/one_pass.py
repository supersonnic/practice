# WRONG SOLUTION
from LinkedList import LinkedList, Node

def sum_lists(l1, l2):
    num1 = get_num(get_digits(l1))
    num2 = get_num(get_digits(l2))
    sum = num1 + num2
    sum_digits = [int(x) for x in str(sum)]
    sum_digits.reverse()
    if len(sum_digits) == 0:
        return None
    sum_list = LinkedList(Node(sum_digits[0]))
    for i in range(1, len(sum_digits)):
        sum_list.add_node(Node(sum_digits[i]))
    return sum_list

def get_digits(list):
    digits = []
    current = list.head
    if current == None:
        return 0
    while current.next != None:
        digits.append(current.value)
        current = current.next
    digits.append(current.value)
    return digits

def get_num(digits):
    num = 0
    for i in range(len(digits)):
        num += digits[i] * (10 ** i)
    return num

### Tests
l1 = LinkedList(Node(7))
l1.add_nodes([Node(1), Node(6)])
l2 = LinkedList(Node(5))
l2.add_nodes([Node(9), Node(2)])
print(l1)
print(l2)
print(sum_lists(l1, l2))
print("\n")

l1 = LinkedList(Node(7))
l2 = LinkedList(Node(5))
print(l1)
print(l2)
print(sum_lists(l1, l2))
print("\n")

l1 = LinkedList(Node(0))
l1.add_nodes([Node(1), Node(6)])
l2 = LinkedList(Node(5))
print(l1)
print(l2)
print(sum_lists(l1, l2))
print("\n")

l1 = LinkedList(Node(7))
l1.add_nodes([Node(1), Node(6), Node(3)])
l2 = LinkedList(Node(5))
l2.add_nodes([Node(9), Node(2)])
print(l1)
print(l2)
print(sum_lists(l1, l2))
print("\n")

l1 = LinkedList(Node(7))
l1.add_nodes([Node(1), Node(6)])
l2 = LinkedList(Node(0))
print(l1)
print(l2)
print(sum_lists(l1, l2))
print("\n")
