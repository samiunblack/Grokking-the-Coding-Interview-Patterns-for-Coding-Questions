from linked_list_cycle import Node

def rearrange(head):
    if head is None or head.next is None:
        return head
    
    slow, fast = head, head
    
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    
    head_second_half = reverse(slow)
    head_first_half = head
    
    while head_first_half is not None and head_second_half is not None:
        next = head_first_half.next
        head_first_half.next = head_second_half
        head_first_half = next
        
        reverse_next = head_second_half.next
        head_second_half.next = head_second_half
        head_second_half = reverse_next
    
    if head_first_half is not None:
        head_first_half.next = None
    

def reverse(head):
    prev = None
    
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    
    return prev

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    
    arranged = rearrange(head)
    
    print_linkedlist(arranged)
    
def print_linkedlist(head):
    while head != None:
        print(head.value)
        head = head.next
    
main()