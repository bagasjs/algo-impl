from __future__ import annotations

class TreeNode:
    value: int
    left: TreeNode | None
    right: TreeNode | None

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def in_order_recursive(root: TreeNode) -> list[int]:
    result = []

    def traverse(node: TreeNode | None):
        if node is None:
            return
        traverse(node.left)      # Recurse on the left subtree
        result.append(node.value)  # Visit the current node
        traverse(node.right)     # Recurse on the right subtree

    traverse(root)
    return result

def in_order_nonrecursive(root: TreeNode) -> list[int]:
    result = []

    stack = [(root, False)]
    while len(stack) > 0:
        node, visited = stack.pop()
        if node is None:
            continue

        if not visited:
            stack.append((node.right, False))
            stack.append((node, True))
            stack.append((node.left, False))
        else:
            result.append(node.value)
    return result


# Example usage
# Construct a binary tree:
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(20)))

print("Recursive in-order traversal:", in_order_recursive(root))
print("Non-Recursive in-order traversal:", in_order_nonrecursive(root))
# Output: [4, 2, 5, 1, 3]

def pre_order_recursive(root: TreeNode) -> list[int]:
    result = []

    def traverse(node: TreeNode | None):
        if node is None:
            return
        result.append(node.value)  # Visit the current node
        traverse(node.left)      # Recurse on the left subtree
        traverse(node.right)     # Recurse on the right subtree

    traverse(root)
    return result

def pre_order_nonrecursive(root: TreeNode) -> list[int]:
    result = []

    stack = [(root, False)]
    while len(stack) > 0:
        node, visited = stack.pop()
        if node is None:
            continue

        if not visited:
            stack.append((node.right, False))
            stack.append((node.left, False))
            stack.append((node, True))
        else:
            result.append(node.value)
    return result

# Example usage
print("Recursive pre-order traversal:", pre_order_recursive(root))
print("Non-Recursive pre-order traversal:", pre_order_nonrecursive(root))
# Output: [1, 2, 4, 5, 3]
