# Depth First Search - Graph Algo 
# Explores Deep instead of wide

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def DFS(root):
    if not root:
        return
    if not root.left and not root.right:
        print(root.val)
        return
    
    DFS(root.left)
    DFS(root.right)


# Example Tree Structure:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Test DFS
DFS(root)

