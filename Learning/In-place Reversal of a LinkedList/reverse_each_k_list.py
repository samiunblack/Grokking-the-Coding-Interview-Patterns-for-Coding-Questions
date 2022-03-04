from reverse_linkedList import Node

def reverse_every_k_element(head, K):
    
    current, previous = head, None
    
    while True:
        last_node_of_first_part = previous
        last_node_of_sublist = current
        
        next = None
        i = 0
        while current is not None and i < K:
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1
        
        if last_node_of_first_part is not None:
            last_node_of_first_part.next = previous
        else:
            head = previous
        
        last_node_of_sublist.next = current
    
        if current is None:
            break
        previous = last_node_of_sublist
    
    return head

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    head.print_list()
    
    reverse_every_k_element(head, 3).print_list()

main()