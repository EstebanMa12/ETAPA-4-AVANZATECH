def odd_even_list(head):
    if not head or not head.next:
        return head  # No hay nodos o solo hay un nodo

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head

    return head

if __name__ == "__main__":
    from linked_list import LinkedList
    myList = LinkedList()
    myList.append(1)
    myList.append(2)
    myList.append(3)
    myList.append(4)
    myList.append(5)
    myList.append(6)
    myList.append(7)
    myList.append(8)
    odd_even_list(myList.first)
    print(myList)

