# Depth-First Search (DFS) is an algorithm used to traverse or search through graph or tree data structures. 
# It explores as far as possible along a branch (depth) before backtracking and exploring other branches.

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self


    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array   