from node import Node

class LinkedList:
    def __init__(self):
        self.first = None
        self.size = 0

    def append(self, Value):
        MyNode = Node(Value)
        if self.size  == 0:
            self.first  = MyNode
        else: 
            current = self.first
            while current.next is not None: 
                current = current.next
            
            current.next  = MyNode
        self.size +=1

        return MyNode

    def remove(self, value):
        if self.size == 0:
            return False
        
        else:
            current = self.first
            try: 
                while current.next.data != value:
                    if current.next == None:
                        return False
                    else:
                        current = current.next
                deletedNode = current.next
                current.next = deletedNode.next
            except AttributeError:
                return False  
        
        self.size -= 1
        return deletedNode
    
    def insert(self, value, position):
        myNode  = Node(value)
        if position == 0:
            myNode.next = self.first 
            self.first = myNode
        else: 
            current = self.first
            k=1
            while current.next is not None and k < position:
                current = current.next
                k +=1
            myNode.next  = current.next
            current.next = myNode

    def __len__(self):
        return self.size

    def __str__(self):
        string = "["
        current = self.first
        for i in range(len(self)):
            string += str(current)
            if i != len(self)-1:
                string += str(", ")
            current = current.next
        string += "]"

        return string


if __name__ == "__main__":
    myList = LinkedList()
    myList.append(1)
    myList.append(2)
    myList.append(3)

    print(myList)

    myList.remove(10)

    myList.insert('A', 3)
    print(myList)
