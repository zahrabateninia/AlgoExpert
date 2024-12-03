#!/usr/bin/env python3

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Divide and Conquer approach: T: O(N), S: O(d) depth of the tree

def validateBst(tree):
    validateBstHelper(tree, float('-inf'), float('inf'))

def validateBstHelper(tree, minValue, maxValue):
    # Check if we are on the leaf node 
    if tree is None:
        return True # if a tree is none it's a valid BST
