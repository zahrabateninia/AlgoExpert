class Node {
    constructor(name){
        this.name = name;
        this.children = []
    }

    addChild(name){
        this.children.push(new Node(name));
        return this;
    }

    depthFirstSearch(array=[]){
        array.push(this.name)
        this.children.forEach((child) => this.depthFirstSearch(array));
        return array;
    }
}

// Space Complexity = O(v) v is the number of vertices(nodes)

// Time complexity = O(v+E) E is number of edges