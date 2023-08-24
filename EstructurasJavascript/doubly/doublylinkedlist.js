class twoWayNode {
    constructor(value) {
        this.value = value;
        this.next = null;
        this.previous = null;
    }
}
class MyDoublyLinkedList {
    constructor(value){
        this.head={
            value: value,
            next: null,
            previous: null,
        }
        this.tail = this.head;
        this.length = 1;
    }
    append(value){
        const newNode = new twoWayNode(value)
        newNode.previous = this.tail;
        this.tail.next = newNode;
        this.tail = newNode;
        this.length++;
        return this;
    }
    prepend(value){
        const newNode = new twoWayNode(value)
        newNode.next = this.head;
        this.head.previous = newNode;
        this.head = newNode;
        this.length++;
        return this;
    }
    insert(value, position){
        if(position >= this.length){
            return this.append(value);
        }
        const newNode = new twoWayNode(value);
        const firstPointer = this.getTheIndex(position - 1);
        const holdingPointer = firstPointer.next;
        firstPointer.next = newNode;
        newNode.previous = firstPointer;
        newNode.next = holdingPointer;
        holdingPointer.previous = newNode;
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

const myDoublyList = new MyDoublyLinkedList(1);
console.log(myDoublyList);
myDoublyList.append(3);
console.log(myDoublyList);
