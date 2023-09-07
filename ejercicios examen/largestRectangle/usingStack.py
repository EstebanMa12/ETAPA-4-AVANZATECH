class Node:
    def __init__(self, data, next=None):
        # Atributos
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        newNode = Node(data)
        if self.top:
            newNode.next = self.top
            self.top = newNode
        else:
            self.top = newNode
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
            return None
    def peek(self):
        if self.top:
            return self.top.data
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
            
def largestRectangleArea(heights):
    stack = Stack()
    maxArea = 0
    i = 0
    while i < len(heights):
        if stack.size == 0 or heights[stack.peek()] <= heights[i]:
            stack.push(i)
            i += 1
            print(f"Round {i} Stack = > {stack}")
        else:
            top = stack.pop()
            if stack.size == 0:
                area = heights[top] * i
            else:
                area = heights[top] * (i - stack.peek() - 1)
            maxArea = max(maxArea, area)
            print(f"max area {maxArea}")
    while stack.size != 0:
        top = stack.pop()
        if stack.size == 0:
            area = heights[top] * i
        else:
            area = heights[top] * (i - stack.peek() - 1)
        maxArea = max(maxArea, area)
        print(f"max area {maxArea}")
    return maxArea

if __name__ == "__main__":
    heights = [0,5,6,6,8,8]
    print(largestRectangleArea(heights))