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
            if value < currentNode.value:
                # we always wanna keep track of the parent node
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else: # when we find the value we wanna remove:
                # if the node we wanna remove has two left and right children
                if currentNode.right is not None and currentNode.left is not None:
                    # we need to find the smallest left-most value in the right subtree and replace it with the node we wanna remove
                    currentNode.value = currentNode.right.getMinValue()
                    # remove the smallest value of the right subtree
                    currentNode.right.remove(currentNode.value, currentNode) # passing currentNode as parent 
                elif parentNode is None:
                    # if the node we wanna remove is the root node so it doesn't its parentNode is None
                    # it has either 1 left/right node or no node at all (we already handled the case with 2 children)
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.right = currentNode.right.left
                        currentNode.left = currentNode.right.right
                    else: # when there is no parentNode and no children for a node 
                        # this is a single-node tree; do nothing. if you remove it you delete the BST!
                        pass

                elif parentNode.left == currentNode: #currentNode is the left child of our parentNode
                    parentNode.left = (
                        currentNode.left if currentNode.left is not None else currentNode.right
                    )
                elif parentNode.right == currentNode:
                    parentNode.right = (
                        currentNode.left if currentNode.left is not None else currentNode.right
                    )
                break

        return self


    def getMinValue(self):
        pass
