from TreeNode import TreeNode

def bfs(root):
    if not root:
        return []
    level, children, nodes = 0, 0, 1
    levels = [[root],[]]
    levels_output = [[root.val],[]]
    added = True
    while added:
        added = False
        for i in range(nodes):
            node = levels[level][i]
            if node.left:
                levels[level + 1].append(node.left)
                levels_output[level + 1].append(node.left.val)
                children += 1
                added = True
            if node.right:
                levels[level + 1].append(node.right)
                levels_output[level + 1].append(node.right.val)
                children += 1
                added = True
        if added:
            nodes = children
            children = 0
            level += 1
            levels.append([])
            levels_output.append([])
    return levels_output[:-1]




tree = TreeNode('a')
tree.left = TreeNode('b')
tree.right = TreeNode('c')
tree.left.left = TreeNode('d')
tree.left.right = TreeNode('e')
tree.right.left = TreeNode('f')
tree.right.right = TreeNode('g')
tree.left.right.left = TreeNode('h')
tree.left.right.right = TreeNode('i')
tree.right.left.right = TreeNode('k')
tree.left.right.right.left = TreeNode('j')

print('Level order:')
print(bfs(tree))
