# Implement a tree
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self,child_node):
        self.children.append(child_node)
    
    # Without __repr__, the output shows the memory address, which isn't very helpful.
    def __repr__(self): 
        return f"Node({self.value})" 

root = Node("Root")
child1 = Node("Child1")
child2 = Node("Child2")
grandchild3 = Node("GrandChild3")

root.add_child(child1)
root.add_child(child2)
child2.add_child(grandchild3)
print(root)
print(root.children)
print(child2.children)

# Implement a Basic Binary Tree
# For every node in the tree:
# The value of all nodes in the left subtree is less than the value of the current node.
# The value of all nodes in the right subtree is greater than the value of the current node.
class BTNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Inserting into a Binary Tree

def BT_Insert_Node(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = BT_Insert_Node(root.left,value)
    else:
        root.right = BT_Insert_Node(root.right,value)
    return root

# Tree Traversals (Implement the following traversal methods)
# Traversal means visiting all the nodes in some order. Common traversal methods are:

# 1. Inorder (Left, Root, Right)
# Used to retrieve elements from a binary search tree (BST) in sorted order.
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)

# 2. Preorder (Root, Left, Right)
def preorder_traversal(node):
    if node:
        print(node.value, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

# 3. Postorder (Left, Right, Root)
def preorder_traversal(node):
    if node:
        preorder_traversal(node.left)
        preorder_traversal(node.right)
        print(node.value, end=" ")

# 4. Level-order (Breadth-first)
from collections import deque

def level_order_traversal(root):
    if root is None:
        return

    # Initialize a queue and add the root node to it
    queue = deque([root])

    # While the queue is not empty, process nodes
    while queue:
        # Dequeue the front node
        node = queue.popleft()
        
        # Visit the node (print its value)
        print(node.value, end=" ")

        # Enqueue left child if it exists
        if node.left:
            queue.append(node.left)
        
        # Enqueue right child if it exists
        if node.right:
            queue.append(node.right)

# Practice Problems
# 1. Implement a function to calculate the height of a tree.
def maxDepth(root):
    if root is None:
        return 0
    
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    return max(left_depth,right_depth) + 1

# 2. Check if a binary tree is balanced.

# 3. Find the lowest common ancestor (LCA) of two nodes in a binary tree.

# 4. Implement a binary search tree (BST) and include search functionality.

# 5. Count the number of leaf nodes in a tree.
