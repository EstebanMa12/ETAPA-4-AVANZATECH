class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for _ in range(capacity):
            self.items.append(fill_value)
        
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, new_item):
        self.items[index] = new_item
    
    def remove(self, value=None, position=None):
        if position is None and value is None:
            raise TypeError('You must specify a value or a position')
        
        if value is not None:
            self.items.remove(value)
        elif position is not None:
            if not isinstance(position, int):
                raise TypeError('Position must be an integer')
            if position < 0 or position >= len(self.items):
                raise IndexError('Position out of range')
            self.items.pop(position)
    
        return self.items
    
    def insert(self, value, position):
        self.items.append(None)
        for i in range(len(self.items)-1, position, -1):
            self.items[i] = self.items[i-1]
        self.items[position] = value
        return self.items
    
    def index(self, value):
        for index, item in enumerate(self.items):
            if item == value:
                return index
        return "Value not found"
            
    def reverse(self):
        return self.items[::-1]
    
    def reverseLoop(self, start=0, end=None):
        if end is None:
            end = len(self.items)-1

        while start < end:
            self.items[start], self.items[end] = self.items[end], self.items[start]
            start += 1
            end -= 1
        return self.items
    def reverseRecursive(self, start=0, end=None):
        if end is None:
            end = len(self.items)-1

        if start < end:
            self.items[start], self.items[end] = self.items[end], self.items[start]
            self.reverseRecursive(start +1, end -1)
        return self.items



if __name__=='__main__':
    a1 = Array(10,'A')
    print(a1)
    print(len(a1))
    print(a1[0])
    a1[0] = 'B'
    print(a1.remove(position = 3))
    print(a1.remove(value = "A"))
    print(a1.insert('C', 3))
    print(a1.index('C'))
    print(a1.reverse())
    print(a1.reverseLoop())
    print(a1.reverseLoop(2, 5))
    print(a1.reverseLoop(start=3))
    print(a1.reverseRecursive())
    


