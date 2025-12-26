#Find the lowest common ancestor of two nodes in a binary tree.

"""
Logic

LCA = first common parent of two nodes.
Useful in networks, file systems, org charts."""




# Node class
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Lowest Common Ancestor function
def lca(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root
    return left if left else right


# Build sample tree
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

# Test LCA
print("\nLCA of 4 and 5:", lca(root, root.left.left, root.left.right).val)  # ✅ Output: 2
print("LCA of 4 and 3:", lca(root, root.left.left, root.right).val)        # ✅ Output: 1
