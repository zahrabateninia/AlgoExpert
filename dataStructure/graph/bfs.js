class Node {
    constructor(name) {
      this.name = name;
      this.children = [];
    }
  
    addChild(name) {
      this.children.push(new Node(name));
      return this;
    }
    
    breadthFirstSearch(array) {
         let queue = [this]; // initialize the queue with the root node
  
          while (queue.length > 0) {
              const currentNode = queue.shift(); // Dequeue the first node
              array.push(currentNode.name); // Add the current node's name to the result
      
              // Enqueue children of the current node
              currentNode.children.forEach(child => queue.push(child));
          }
      
          return array;
        }
  }
  
//   My Note:
// The this keyword in JavaScript refers to the current context, typically the object that owns the method being executed
// By initializing the queue with this, you're explicitly starting the traversal from the root node of the tree