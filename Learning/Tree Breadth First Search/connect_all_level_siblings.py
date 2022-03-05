class TreeNode:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left, self.right = left, right
        self.next = next
    
    def print_tree(self):
        print("Traversal using next pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next

def connect_all_level_siblings(root):
    queue = [root]
    prev_node = None
    
    while len(queue) > 0:
        level_size = len(queue)
        
        for _ in range(level_size):
            current = queue.pop(0)
            
            if prev_node:
                prev_node.next = current
            prev_node = current
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
                
def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_level_siblings(root)
    root.print_tree()

main()                