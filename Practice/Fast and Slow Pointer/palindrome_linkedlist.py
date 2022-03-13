class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_palindrome(head):
    slow, fast = head, head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    middle = slow
    
    slow, fast = head, reverse(middle.next)
    
    reverse(middle.next)
    
    while fast:
        if slow.value == fast.value:
            slow = slow.next
            fast = fast.next
        else:
            return False    
    return True
    

def reverse(head):
    current = head
    prev = None
    
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    
    return prev

def main():
    list = Node(2, Node(4, Node(6, Node(4, Node(2)))))
    print("Is palindrome: " + str(find_palindrome(list)))
    
    list = Node(2, Node(4, Node(6, Node(4, Node(2, Node(2))))))
    print("Is palindrome: " + str(find_palindrome(list)))

    
main()