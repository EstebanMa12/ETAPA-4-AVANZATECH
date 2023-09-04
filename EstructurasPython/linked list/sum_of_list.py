
def sum_of_list(head1, head2):
    from node import Node
    temp = Node()
    current1 = head1
    current2 = head2
    current = temp
    while current1 or current2: 
        if current1 and current2:
            current.data = (current1.data + current2.data)%10
            print(f"Suma = {current.data}")
        elif current1:
            current.data = current1.data
        else:
            current.data = current2.data
        if current1:
            current1 = current1.next
        if current2:
            current2 = current2.next
        print(f"Current = {current}")
        current.next = Node()
        current = current.next

    return temp
if __name__=="__main__":
    from linked_list import LinkedList
    head1 = LinkedList()
    head2 = LinkedList()
    head1.append(3)
    head1.append(1)
    head1.append(5)
    head2.append(5)
    head2.append(9)
    head2.append(2)
    a =sum_of_list(head1.first, head2.first)
    print(a)
