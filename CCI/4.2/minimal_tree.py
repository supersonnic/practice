import math
from TreeNode import TreeNode

def make_tree(s, e, nums):
    if s > e:
        return
    mid = math.ceil(s + ((e - s) // 2))
    node = TreeNode(nums[mid])
    node.left = make_tree(s, mid - 1, nums)
    node.right = make_tree(mid + 1, e, nums)
    return node

nums = [0, 1, 2, 3, 4, 5, 6]
tree = make_tree(0, len(nums) - 1, nums)
print('\nInorder:')
tree.inorder(tree)

nums = [0, 1, 2, 3, 4, 5, 6, 7]
tree = make_tree(0, len(nums) - 1, nums)
print('\nInorder:')
tree.inorder(tree)
