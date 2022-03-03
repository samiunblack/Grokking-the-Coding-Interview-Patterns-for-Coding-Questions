class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()

def reverse_sublist(head, p, q):
    current = head
    prev = None
    
    i = 0
    while current is not None and i < p - 1:
            prev = head
            current = head.next
            i += 1
            
    last_node_of_first_part = prev
    first_node_of_last_part = current
    
    i = 0
    
    while current is not None and i < q - p + 1:
        next = current.next
        
        current.next = prev
        prev = current
        current = next
        i += 1
    
    if last_node_of_first_part is not None:
        last_node_of_first_part.next = prev
    else:
        head = prev
    
    first_node_of_last_part.next = current
    
    return head
        

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    result = reverse_sublist(head, 2, 4)
    result.print_list()
    
main()