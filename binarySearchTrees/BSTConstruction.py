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

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self
