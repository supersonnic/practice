from TreeNode import TreeNode

def preorder(root: TreeNode):
    stack, output = [root], []
    while stack:
        item = stack.pop()
        output.append(item.val)
        if item.right:
            stack.append(item.right)
        if item.left:
            stack.append(item.left)
    return output

def inorder(root: TreeNode):
    stack, output = [root], []
    while stack:
        item = stack[-1]
        if item.right:
            stack.append(item.right)
            continue
        if

def postorder(root: TreeNode):
    

# Creating the tree
tree = TreeNode('a')
tree.left = TreeNode('b')
tree.right = TreeNode('e')
tree.left.left = TreeNode('c')
tree.left.right = TreeNode('d')
tree.right.left = TreeNode('f')
tree.right.right = TreeNode('g')

# Tests
print('Preorder')
print(preorder(tree))
# print('Inorder')
# inorder(tree)
# print('Postorder')
# postorder(tree)
