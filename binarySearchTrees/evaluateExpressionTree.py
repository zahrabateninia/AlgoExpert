# You're given a binary expression tree, write a function to evaluate this tree mathematically and return a single resulting int
# All leaf nodes in the tree represent operands, which are positive ints.
# All of the other nodes represent operands, there are 4 operators supported: -1(addition),-2(subtraction),-3(division),-4(multiplication)
# Each operator also works as a grouping symbol

# O(n) time| O(h) space

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    # Write your code here.
    return -1