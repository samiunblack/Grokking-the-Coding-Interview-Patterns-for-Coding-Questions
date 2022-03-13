class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    if head is None or head.next is None:
        return False
    
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False

def main():
    list = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
    print("Linked List has cycle: " + str(has_cycle(list)))
    
    list.next.next.next.next.next.next = list.next.next
    print("Linked List has cycle: " + str(has_cycle(list)))
    
main()