from reverse_linkedList import Node

def reverse_first_k_elements(head, k):
    prev, current = None, head
    
    last_part = current
    
    i = 1
    while current is not None and i <= k:
        next = current.next
        current.next = prev
        prev = current
        current = next
        
        i += 1
    
    head = prev
    last_part.next = current
    
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head.print_list()
    
    reverse_first_k_elements(head, 4).print_list()

main()
