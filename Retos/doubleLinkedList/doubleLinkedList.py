from node import Node, TwoWayNode

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size

    def __str__(self):
        if self.size ==0:
            return "[]"
        string = "["
        current = self.head
        for node in range(self.size):
            string += f"{current}"
            if node != self.size -1:
                string+= ", "
            current = current.next
        string += "]"
        return string
    # add a new element to the end of list

    def append(self, data):
        newNode=TwoWayNode(data)
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.previus = self.tail
            self.tail.next = newNode
            self.tail = newNode
            # self.head.previus = newNode
            # newNode.next = self.head
        self.size +=1

    def Relations(self):
        if self.size ==0:
            print("No relationships were found")
        else:
            current = self.head
            for i in range(self.size):
                print(f"Prev({current.previus}) --> Current({current}) --> Next({current.next})") 
                current = current.next

    def insert(self, data, position):
        newNode = TwoWayNode(data)
        if position ==0:
            newNode.next = self.head
            self.head.previus = newNode
            self.head=newNode
        elif position == self.size:
            self.tail.next = newNode
            newNode.previus = self.tail
            self.tail = newNode

        else:
            count =1
            current  = self.head
            while current.next is not None and count < position:
                current = current.next
                count += 1
            newNode.next = current.next
            newNode.previus = current
            current.next = newNode
            current.next.previus = newNode


        self.size +=1



        
