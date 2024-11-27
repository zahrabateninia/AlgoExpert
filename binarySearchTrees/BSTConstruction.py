# the insert, contains, and remove methods
# Average: T: O(log(N)) (we eliminate the half), S: O(log(N)) (if implemented recursively), but iteratively: S: O(1)
# Worst: T: O(N) , S: O(N) (if implemented recursively), but iteratively: S: O(1)
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self
        while True:
            if currentNode.value < value:
                if currentNode.value == None:
                    currentNode.left = BST(value)
                    break # get out of the loop after inserting
                else:
                    currentNode = currentNode.left
            
            else:
                if currentNode.right ==  None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right

        return self

    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if currentNode.value < value:
                currentNode = currentNode.right
            elif currentNode.value > value:
                currentNode = currentNode.left
            else: 
                return True
            return False

    def remove(self, value, parentNode = None):
        currentNode = self
        while currentNode is not None:
            if currentNode.value < value:
                # we always wanna keep track of the parent node
                parentNode = currentNode
                currentNode = currentNode.right
            elif currentNode.value > value:
                parentNode = currentNode
                currentNode = currentNode.left
            else: # when we find the value we wanna remove:
                # if the node we wanna remove has two left and right children
                if currentNode.right is not None and currentNode.left is not None:
                    # we need to find the smallest left-most value in the right subtree and replace it with the node we wanna remove
                    currentNode.value = currentNode.right.getMinValue()
                    # remove the smallest value of the right subtree
                    currentNode.right.remove(currentNode.value, currentNode) # passing currentNode as parent 

        return self
