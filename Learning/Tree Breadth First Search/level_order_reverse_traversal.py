class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

def reverse_traversal(root):
    queue = [root]
    result = []
    
    while queue != []:
        levelsize = len(queue)
        current_level = []
        
        for _ in range(levelsize):
            current = queue.pop(0)

            current_level.append(current.val)
            
            if current.left:
                queue.append(current.left)
            
            if current.right:
                queue.append(current.right)
            
        result.insert(0, current_level)
    
    return result
    
    
def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    
    reverse_traversal(root)
    print("Level order traversal: " + str(reverse_traversal(root)))
    
main()