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
    
    def __len__(self):
        return self.size


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

    def insert(self, data, position):
        assert isinstance (position , int), 'Position must be an integer'
        newNode = Node(data)
        if len(self)==0 or position==0 :
            newNode.next = self.head
            self.head = newNode
            self.size +=1

        elif position > self.size:
            raise IndexError("Index out of bounds")
        
        else:
            current = self.head 
            counter =1
            while current.next is not None and counter < position:
                current = current.next
                counter +=1
            newNode.next = current.next
            current.next = newNode
            self.size += 1

    def replace(self,data, position):
        """Replace value at given index"""
        newNode = Node(data)
        assert isinstance (position ,int ),"Position must be an Integer."
        if len(self)==0 or position<0 or position > self.size :
            raise IndexError ("index Out Of Bounds.")
        if position == 0:
            current = self.head
            self.head = newNode
            newNode.next = current.next
        else:
            current = self.head
            count = 1
            while current !=None and count < position:
                current =current.next
                count+=1
            previus_node = current
            next_node =previus_node.next.next
            previus_node.next = newNode
            newNode.next=next_node

    def delete(self, data):
        current = self.head
        if self.size ==0:
            return False
        elif current.data ==data:
            self.head = current.next
        else:
            try:
                while current.next.data != data:
                    if current.next == None:
                        return False
                    else:
                        current = current.next
                current.next =  current.next.next
            except AttributeError:
                return False
        self.size -= 1

        