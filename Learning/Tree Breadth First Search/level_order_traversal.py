class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

def traverse(root):
    result = []
    queue = [root]
    
    while queue != []:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            current = queue.pop(0)
            
            current_level.append(current.val)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        result.append(current_level)
    
    return result
    

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    
    print("Level order traversal: " + str(traverse(root)))
    
main()