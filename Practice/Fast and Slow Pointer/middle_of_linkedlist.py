class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_middle(head):
    if head is None or head.next is None:
        return head
    
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.value

def main():
    list = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    print("Linked List middle: " + str(find_middle(list)))
    
    list = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
    print("Linked List middle: " + str(find_middle(list)))
    
    list = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))
    print("Linked List middle: " + str(find_middle(list)))
    
main()