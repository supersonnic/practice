from TreeNode import TreeNode

tree = TreeNode('a')
tree.left = TreeNode('b')
tree.right = TreeNode('e')
tree.left.left = TreeNode('c')
tree.left.right = TreeNode('d')
tree.right.left = TreeNode('f')
tree.right.right = TreeNode('g')

print('Preorder:')
tree.preorder(tree)
print('\nInorder:')
tree.inorder(tree)
print('\nPostorder:')
tree.postorder(tree)
