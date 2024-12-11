# Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost 
# branch sum to rightmost branch sum.

# A branch sum is the sum of all values in a Binary Tree branch. A binary Tree branch is a path of nodes in a tree
# that starts at the root node and ends at tny leaf node.

# T: O(n), S: O(n)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    calculateBranchSum(root, 0, sums)
    return sums
    
def branchSums(root):
    sums = []
    calculateBranchSum(root, 0, sums)
    return sums

def calculateBranchSum(node, runningSum, sums):
    # base case
    if node is None:
        return

    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    calculateBranchSum(node.left, newRunningSum, sums)
    calculateBranchSum(node.right, newRunningSum, sums)
    



    