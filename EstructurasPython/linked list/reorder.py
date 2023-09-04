from ispalindrome import reverse

def reorder(head):
  if not head or not head.next: return head
  slow = head
  fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  reverse_part= reverse(slow)
  while head and reverse_part:
    temp = head.next
    head.next = reverse_part
    head = temp
    temp = reverse_part.next
    reverse_part.next = head
    reverse_part = temp
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
  print(reorder(myList.first))
  print(myList)