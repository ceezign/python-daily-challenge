# Good morning! Here's your coding interview problem for today.
# This problem was asked by Google.
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_unival_subtrees(root):
    count, _ = helper(root)
    return count

def helper(node):
    if node is None:
        return 0, True # count = 0, is_unival = True (empty tree is unival)

    left_count, is_left_unival = helper(node.left)
    right_count, is_right_unival = helper(node.right)

    total_count = left_count + right_count

    # check if the current node is unival
    if is_left_unival and is_right_unival:
        if node.left and node.left.val != node.val:
            return  total_count, False
        if node.right and node.right.val != node.val:
            return total_count, False
        # Current subtree is unival
        return total_count + 1, True
    return total_count, False

root = Node(0)
root.left = Node(1)
root.right = Node(0)
root.right.left = Node(1)
root.right.right = Node(0)
root.right.left.left = Node(1)
root.right.left.right = Node(1)


print(count_unival_subtrees(root))