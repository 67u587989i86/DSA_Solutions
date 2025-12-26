""" 
Binary Tree -- BInary tree is a tree data structure in which each node has at most two children, 
referred to as the left child and the right child. 
The height of a binary tree is defined as the length of 
     the longest path from the root node to a leaf node. 
The height of an empty tree is -1, and the height of a tree with only one node (the root) is 0.
"""

#Height = max depth of tree.
#Useful to analyze tree balance, performance of operations.



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))


# Example: Build a simple binary tree
#         1
#        / \
#       2   3
#      / \
#     4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("\nHeight of tree:", height(root))

