class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class MySinglyLinkedList {
    constructor(value) {
        this.head = {
        value: value,
        next: null,
        };
        this.tail = this.head;

        this.length = 1;
    }
    append(value){
        const newNode = new Node(value);
        this.tail.next = newNode;
        this.tail = newNode;
        this.length++;
        return this; // return the linked list
    }
    prepend(value){
        const newNode = new Node(value);
        newNode.next = this.head;
        this.head = newNode;
        this.length++;
        return this; // return the linked list
    }
    insert(value, position){
        if(position >= this.length){
            return this.append(value);
        }
        const newNode = new Node(value);
        const firstPointer = this.getTheIndex(position - 1);
        const holdingPointer = firstPointer.next;
        firstPointer.next = newNode;
        newNode.next = holdingPointer;
        this.length++;
        return this; // return the linked list
    }
    getTheIndex(index){
        let current = this.head;
        let count = 0;
        while(count !== index){
            current = current.next;
            count++;
        }
        return current
    }
}
const myList = new MySinglyLinkedList(1);
console.log(myList);
myList.append(3);
console.log(myList);
myList.prepend(0);
console.log(myList);
myList.insert(1.5, 2);
console.log(myList);