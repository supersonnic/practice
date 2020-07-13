class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

    def preorder(self, root):
        if root:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val)
