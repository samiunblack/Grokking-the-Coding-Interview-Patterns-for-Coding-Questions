from reverse_llinkedList import Node

def reverse_sublist(head, p, q):
    prev = None
    current = head
    
    i = 1
    while current is not None and i < p:
        prev = current
        current = current.next
        
        i += 1
    
    first_part = prev
    last_part = current
    
    while current is not None and i < q + 1:
        next = current.next
        current.next = prev
        prev = current
        current = next
        
        i += 1
    
    first_part.next = prev
    last_part.next = current
    
    return head

    
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head.print_list()
    
    reverse_sublist(head, 2, 4).print_list()
    
main()
        