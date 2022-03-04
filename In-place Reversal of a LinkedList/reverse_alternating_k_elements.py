from reverse_linkedList import Node

def reverse_alternating_k_elements(head, K):
    if K <= 1 or head is None:
        return head
    
    current, prev = head, None
    
    while True:
        last_node_of_previous = prev
        last_node_of_sublist = current
        
        i = 0
        while current is not None and i < K:
            next = current.next
            current.next = prev
            prev = current
            current = next
            
            i += 1
        
        if last_node_of_previous is not None:
            last_node_of_previous.next = prev
        else:
            head = prev
        
        last_node_of_sublist.next = current
        
        i = 0
        while current is not None and i < K:
            prev = current
            current = current.next
            
            i += 1
        
        if current is None:
            break
    
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
    
    reverse_alternating_k_elements(head, 2).print_list()

main()