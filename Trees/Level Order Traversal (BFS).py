"""
Logic-

Uses Queue.
Useful in shortest path, organization hierarchy."""

"""
1. Push root in queue
2. While queue not empty:
   - Pop node
   - Process it
   - Push its children
"""



from collections import deque

# Define Node class
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Level Order Traversal
def level_order(root):
    if not root:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.val, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

# Build a sample tree
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

print("\nLevel Order:")
level_order(root)
