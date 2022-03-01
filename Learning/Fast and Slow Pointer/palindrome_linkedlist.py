from linked_list_cycle import Node

def palindrom_linkedlist(head):
    if head is None or head.next is None:
        return True
    
    
    slow, fast = head, head
    
    #find out the middle of linked list
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
    
    #reverse the second half of linked list
    head_second_half = reverse(slow)
    
    #copy the reversed second half of linked list
    #so we can revert it later
    copy_head_second_half = head_second_half
    
    #compare the current node of first half and second half
    #if it matches then it's palindrome
    while head != None and head_second_half != None:
        if head.value != head_second_half.value:
            break
        
        head = head.next
        head_second_half = head_second_half.next
    
    #revert it back
    reverse(copy_head_second_half)
    
    #when matched the head or head_second_half would go to the last
    if head == None or head_second_half == None:
        return True
    
    return False

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
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = Node(2)
    
    print(palindrom_linkedlist(head))
    
main()