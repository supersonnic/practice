import math
from TreeNode import TreeNode
from LinkedList import LinkedList, Node
from collections import deque

def linked_tree(root):
    level = 1
    q = deque()
    q.append(root)
    while q:
        print(f"This is level {level}")
        l = len(q)
        for _ in range(l):
            node = q.popleft()
            print(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1

tree = TreeNode(4)
tree.left = TreeNode(2)
tree.right = TreeNode(6)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right.left = TreeNode(5)
tree.right.right = TreeNode(7)
# print('\nInorder:')
# tree.inorder(tree)
# linked_list = linked_tree(tree)
# print(linked_list)
linked_tree(tree)
