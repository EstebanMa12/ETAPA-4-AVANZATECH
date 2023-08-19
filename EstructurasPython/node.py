class Node:
    def __init__(self, data, next=None):
        # Atributos
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)
