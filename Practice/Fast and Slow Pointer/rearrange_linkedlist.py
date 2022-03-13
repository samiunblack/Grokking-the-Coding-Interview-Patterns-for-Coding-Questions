class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()

def rearrange(head):
    slow, fast = head, head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    middle = slow
    slow, fast = head, reverse(middle)
    
    while fast:
        slow_next = slow.next
        slow.next = fast
        slow = slow_next
        
        fast_next = fast.next
        fast.next = slow
        fast = fast_next
    
    if slow is not None:
        slow.next = None
        
    

def reverse(head):
    current, prev = head, None
    
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    
    return prev


def main():
    list = Node(2, Node(4, Node(6, Node(8, Node(10, Node(12))))))
    rearrange(list)
    list.print_list()
    
main()