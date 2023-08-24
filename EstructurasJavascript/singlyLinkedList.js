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
}
const myList = new MySinglyLinkedList(1);
console.log(myList);
myList.append(2);
myList.append(3);
console.log(myList);