from doubleLinkedList import DoubleLinkedList

myDoubleLinkedList = DoubleLinkedList()

myDoubleLinkedList.append(4)
myDoubleLinkedList.append(5)
myDoubleLinkedList.append(6)
myDoubleLinkedList.append(8)


print(myDoubleLinkedList)

other = DoubleLinkedList()
other.Relations()

myDoubleLinkedList.insert(0,0)
print("Length of the linked list is: ", myDoubleLinkedList.__len__())
myDoubleLinkedList.insert("A",3)
myDoubleLinkedList.Relations()
print(myDoubleLinkedList)