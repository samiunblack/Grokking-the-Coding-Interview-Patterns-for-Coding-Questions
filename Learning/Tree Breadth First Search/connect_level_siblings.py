class TreeNode:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left, self.right = left, right
        self.next = next
    
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()

def connect_level_siblings(root):
    queue = [root]
    
    while len(queue) > 0:
        level_size = len(queue)
        prev_level = None
        
        for _ in range(level_size):
            current = queue.pop(0)
            
            if prev_level:
                prev_level.next = current
            prev_level = current
            
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
    connect_level_siblings(root)
    
    print("level order traversal using next pointer:")
    root.print_level_order()
    
main()
