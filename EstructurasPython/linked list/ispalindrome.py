def reverse(head):
    if not head or not head.next: return head
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def isPalindrome(head):
    if not head or not head.next: return True
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    slow = reverse(slow)
    while slow:
        if slow.data != head.data:
            return False
        slow = slow.next
        head = head.next
    return True

if __name__ == "__main__":
    from linked_list import LinkedList
    myList = LinkedList()
    myList.append(1)
    myList.append(2)
    myList.append(3)
    myList.append(4)
    myList.append(3)
    myList.append(3)
    myList.append(1)
    print(isPalindrome(myList.first))