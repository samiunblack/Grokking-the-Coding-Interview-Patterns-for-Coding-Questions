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

def reverse_linkedList(head):
    prev = None
    current  = head
    
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    
    return prev

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    
    head.print_list()
    result = reverse_linkedList(head)
    result.print_list()
    

