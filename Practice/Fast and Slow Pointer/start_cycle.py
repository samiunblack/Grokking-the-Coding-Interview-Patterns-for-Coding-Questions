from email import header


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        

def find_cycle_start(head):
    slow, fast = head, head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            cycle_length = find_cycle_length(slow)
            break
    
    return find_start(head, cycle_length)


def find_cycle_length(slow):
    current = slow
    cycle_length = 0
    
    while True:
        cycle_length += 1
        current = current.next
        if current == slow:
            break
    
    return cycle_length
        

def find_start(head, cycle_length):
    slow, fast = head, head
    
    while cycle_length:
        fast = fast.next
        cycle_length -= 1
    
    while fast != slow:
        slow = slow.next
        fast = fast.next
        
    return slow.value

def main():
    list = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
    
    list.next.next.next.next.next.next = list.next.next
    print("Linked List cycle start: " + str(find_cycle_start(list)))
    
    list.next.next.next.next.next.next = list.next.next.next
    print("Linked List cycle start: " + str(find_cycle_start(list)))
    
    list.next.next.next.next.next.next = list
    print("Linked List cycle start: " + str(find_cycle_start(list))) 
    
    
main()