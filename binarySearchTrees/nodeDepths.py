#!/usr/bin/env python3

# A function that takes a binary tree and returns the sum of its nodes' depths
# Note: to get the depth of any particular node we need some extra info from our parent node (except root node that we already know its depth is 0)
# our recursive function : f(node, depthOfNode) = f(leftChildNode, depthOfNode +1) + depthOfNode + f(rightChildNode, depthOfNode + 1) 
# base case: when we are in the leaf node

# Time: O(n) n:total number of nodes in the binary tree
# Space: O(h) h: height of the binary tree (maximum function calls on stack will be the number of height)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def nodeDepths(root, depth = 0):
    # handle the base case of recursion
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)
