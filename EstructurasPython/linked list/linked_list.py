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
        self.size +=1
        return myNode

    def reverse(self, start=0, end= None):
        if end is None:
            end = len(self)-1
        if start == end:
            return self.__str__()
        
        current = self.first
        previous = None
        count = 0
        while count < start:
            previous = current
            current = current.next
            count +=1

        tail = current
        head = None
        while count <= end:
            current.next , previous, current = previous, current, current.next
            count +=1

        if previous:
            previous.next = head
        else:
            self.first = previous


        return self.__str__()
        

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
    print(myList.reverse())
    print(myList.insert("B",2))
    print(myList)
    print(myList.reverse(1,3))