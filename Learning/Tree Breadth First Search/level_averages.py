class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

def level_averages(root):
    queue = [root]
    result = []
    
    while len(queue) > 0:
        level_size = len(queue)
        sum = 0
        
        for _ in range(level_size):
            current = queue.pop(0)
            
            sum += current.val
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        result.append(sum/level_size)
    
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print("Level order traversal: " + str(level_averages(root)))
    
main()