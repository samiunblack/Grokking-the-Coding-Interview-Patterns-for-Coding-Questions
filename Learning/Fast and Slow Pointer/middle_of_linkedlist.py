from linked_list_cycle import Node

def middle_of_linkedlist(head):
    slow, fast = head, head
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    
    print(middle_of_linkedlist(head).value)
    
main()