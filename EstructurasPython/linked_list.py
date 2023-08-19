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
            while current.next.data != value:
                if current.next == None:
                    return False
                else:
                    current = current.next
            deletedNode = current.next
            current.next = deletedNode.next
        self.size -= 1
        return deletedNode

    def __len__(self):
        return self.size

    def __str__(self):
        string = "["
        current = self.first
        while current is not None:
            string += str(current)
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
