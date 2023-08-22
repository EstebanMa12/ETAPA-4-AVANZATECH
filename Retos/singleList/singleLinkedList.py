""" import sys
sys.path.append('Node')

import node """
from node import Node

class singleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __str__(self):
        # print the list
        string = "["
        current = self.head
        for node in range(self.size):
            string += f"{current}"
            if node != self.size -1:
                string+= ", "
            current = current.next
        string += "]"
        return string


    def append(self, data):
        newNode=Node(data) #creating a new node object
        if self.size ==0:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
        self.size += 1