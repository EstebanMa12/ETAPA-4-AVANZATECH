from singleLinkedList import singleLinkedList

mylinkedList = singleLinkedList()

mylinkedList.append(1)
mylinkedList.append(1)
mylinkedList.append(1)
mylinkedList.append(3)
mylinkedList.append(4)
mylinkedList.append(5)


mylinkedList.insert("A",2)
mylinkedList.insert("B",0)
mylinkedList.replace("Z",3)
print(f"Antes de borrar los archivos {mylinkedList}")
mylinkedList.delete("B")
print(f"Despues de borrar B {mylinkedList}")
mylinkedList.delete("Z")
print(f"Despues de borrar Z {mylinkedList}")
print("Length of the linked list is: ", mylinkedList.__len__())
print(mylinkedList)