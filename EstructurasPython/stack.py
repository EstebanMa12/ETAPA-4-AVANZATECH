from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

        self.size += 1
    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return "The stack is empty"    
        
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return "The stack is empty"
        
    def clear(self):
        while self.top:
            self.pop()
            
    def recursiveReverse(self):
        if self.top:
            store_data= self.top.data
            self.pop()
            self.recursiveReverse()
            self.push(store_data)
            return self.__str__
        else:
            return None



    def __str__(self):
        string = "["
        current = self.top
        for i in range(self.size):
            string += str(current)
            if i != self.size-1:
                string += str(", ")
            current = current.next
        string += "]"

        return string


if __name__=="__main__":
    food = Stack()
    food.push("pizza")
    food.push("hamburger")
    food.push("Ham")
    food.push("Hot dog")
    print(food)
    food.pop()
    print(food)
    print(food.peek())
    print(food.recursiveReverse())
