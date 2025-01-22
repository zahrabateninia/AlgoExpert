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
    # base case: we reach a leaf node which here is a positive number
    if tree.value >= 0:
        return tree.value

    # when we reach an operator we wanna first get the values of left and right-subtrees
    # and do whatever the operation is

    leftValue = evaluateExpressionTree(tree.left)
    rightValue = evaluateExpressionTree(tree.right)

    if tree.value == -1:
        return leftValue + rightValue
    if tree.value == -2:
        return leftValue - rightValue
    if tree.value == -3:
        return int(leftValue/rightValue)

    return leftValue * rightValue

    
