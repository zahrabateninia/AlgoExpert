# Take a BST and a target integer value and return the closest value to that target value contained in the BST
# avg Time complexity O(log(N)), worst T: O(N) and Space on worst case O(N) we have n frames on our call stack
#  worst T: O(N) | S: O(N)
# class of input tree
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findClosestValueInBst(tree, target):
    # Solve the question recursively 
    return findClosestValueBstHelper(tree, target, float('inf'))

def findClosestValueBstHelper(tree, target, closest):
    # base case
    if tree is None:
        return closest

    if abs(target - closest) > abs(target - tree.value): 
        closest = tree.value

    if target < tree.value:
        findClosestValueBstHelper(tree.left, target, closest)
    elif target > tree.value:
        findClosestValueBstHelper(tree.right, target, closest)
    return closest