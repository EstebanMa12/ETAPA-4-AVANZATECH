class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right  = null;
    }
}
class BinarySearchTree{
    constructor(){
        this.root = null;
    }
    insert(value){
        const newNode = new Node(value)
        if (this.root === null){
            this.root = newNode;
        }
        else{
            let current = this.root;
            while(true){
                if (value < current.value){
                    if (!current.left){
                        current.left = newNode;
                        return this;
                    }
                    current = current.left;
                }else{
                    if (!current.right){
                        current.right = newNode;
                        return this;
                    }
                    current = current.right;
                }
            }
        }
    }
    search(value){
        if (this.root === null){
            return false;
        }
        else{
            let current = this.root;
            while(true){
                if (value === current.value){
                    return current;
                }
                else if (value < current.value){
                    if (!current.left){
                        return false;
                    }
                    current = current.left;
                }else{
                    if (!current.right){
                        return false;
                    }
                    current = current.right;
                }
            }
        }
    }
}
const tree = new BinarySearchTree();
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
console.log(tree);
console.log(tree.search(4));
