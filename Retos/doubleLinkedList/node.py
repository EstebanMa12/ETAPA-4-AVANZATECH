class Node: 
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)
    
class TwoWayNode(Node):
    def __init__(self, data, previus=None, next=None):
        super().__init__(data,next)
        self.previus = previus

    def __str__(self):
        return str(self.data)