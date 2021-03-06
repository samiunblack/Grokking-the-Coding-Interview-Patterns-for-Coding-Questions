class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

def level_order_successor(root, node):
    queue = [root]
    
    while len(queue) > 0:
        level_size = len(queue)
        
        for _ in range(level_size):
            current = queue.pop(0)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            
            if current.val == node:
                break
            
        return queue[0].val if queue else None


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("Level order successor: " + str(level_order_successor(root, 3)))
    
main()        