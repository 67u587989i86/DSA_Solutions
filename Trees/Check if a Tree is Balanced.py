#A tree is balanced if height difference of left and right ≤ 1 for every node.

"""Logic - 

Balanced tree ensures O(log n) operations.
Used in AVL/Red-Black Trees."""





# Node class
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Function to check if tree is balanced
def is_balanced(root):
    def check(node):
        if not node:
            return 0
        left = check(node.left)
        if left == -1:
            return -1
        right = check(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    return check(root) != -1


# Build a sample tree (balanced)
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

print("\nIs Balanced:", is_balanced(root))  # ✅ Should print True


# Build an unbalanced tree
#         1
#        /
#       2
#      /
#     3

root2 = Node(1)
root2.left = Node(2)
root2.left.left = Node(3)

print("Is Balanced:", is_balanced(root2))  # ❌ Should print False
