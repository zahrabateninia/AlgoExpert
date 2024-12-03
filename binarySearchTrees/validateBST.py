#!/usr/bin/env python3

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Divide and Conquer approach: T: O(N), S: O(d) depth of the tree

def validateBst(tree):
    return validateBstHelper(tree, float('-inf'), float('inf'))

def validateBstHelper(tree, minValue, maxValue):
    # Check if we are on the leaf node 
    if tree is None:
        return True # if a tree is none it's a valid BST

    # according to bst definition every node.value should be greater than min value and strictly smaller than max value, otherwise it's not valid
    if tree.value < minValue or tree.value >= maxValue:
        # if one of these conditions is broken:
        return False

    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
    rightIsValid = validateBstHelper(tree.right, tree.value, maxValue)

    return leftIsValid and rightIsValid
