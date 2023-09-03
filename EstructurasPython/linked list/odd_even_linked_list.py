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
    my_ll = LinkedList()
    my_ll.add(1)
    my_ll.add(2)
    my_ll.add(3)
    my_ll.add(4)
    my_ll.add(5)
    my_ll.add(6)
    my_ll.add(7)
    my_ll.add(8)
    my_ll.add(9)
    my_ll.add(10)