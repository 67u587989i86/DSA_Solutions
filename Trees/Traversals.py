"""
Preorder: Visit node → Traverse left → Traverse right -- also known as root-first traversal
Inorder: Traverse left → Visit node → Traverse right -- also known as symmetric traversal
Postorder: Traverse left → Traverse right → Visit node -- also known as depth-first traversal

Level-order: Visit nodes level by level from top to bottom and left to right -- also known as breadth-first traversal
Depth-first: Explore as far down a branch as possible before backtracking 
Breadth-first: Explore all neighbors at the present depth prior to moving on to nodes at the next depth level

Graph Traversals:
Depth-first search (DFS): Explore as far as possible along each branch before backtracking
Breadth-first search (BFS): Explore all neighbors at the present depth prior to moving on to nodes at the next depth level
"""




class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder(root):
    if not root: return
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if not root: return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

def postorder(root):
    if not root: return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=" ")

# Example
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder:")
preorder(root)
print("\nInorder:")
inorder(root)
print("\nPostorder:")
postorder(root)
