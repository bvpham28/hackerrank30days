def insert(self, head, data):
    # if head is empty, set the head to the first element of the data
    if head is None:
        head = Node(data)
    # if it's not empty, continue on with the list.
    else:
        current = head
        #continue on with the linked list and place them into nodes
        while current.next:
            current = current.next
        current.next = Node(data)
    return head
 