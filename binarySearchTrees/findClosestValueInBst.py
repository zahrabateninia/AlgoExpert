# Take a BST and a target integer value and return the closest value to that target value contained in the BST
# avg Time complexity O(log(N)), worst T: O(N) and Space on worst case O(N) we have n frames on our call stack
#  
# class of input tree
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findClosestValueInBst(tree, target):
