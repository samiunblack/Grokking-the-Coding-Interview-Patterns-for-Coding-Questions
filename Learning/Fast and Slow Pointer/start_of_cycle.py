from linked_list_cycle import Node

def start_of_cycle(head):
    fast, slow = head, head
    
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        
        if fast == slow:
            cycle_length = calculate_cycle_length(slow)
            break
    
    return find_start(head, cycle_length)

def calculate_cycle_length(slow):
    cycle_length = 0
    current = slow
    
    while True:
        current = current.next
        cycle_length += 1
        
        if current == slow:
            break
    
    return cycle_length

def find_start(head, cycle_length):
    ptr1 = head
    ptr2 = head
    
    while cycle_length > 0:
        ptr1 = ptr1.next
        cycle_length -= 1
        
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    return ptr1

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    
    head.next.next.next.next.next.next = head.next.next
    print(start_of_cycle(head).value)
    
    head.next.next.next.next.next.next = head.next.next.next
    print(start_of_cycle(head).value)

main()