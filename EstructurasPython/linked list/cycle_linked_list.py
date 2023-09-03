def cycleLl(head):
    if not head or not head.next:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True
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
    print(cycleLl(myList.first))