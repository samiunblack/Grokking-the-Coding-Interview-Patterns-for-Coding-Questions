class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

def right_view(root):
    queue = [root]
    result = []
    
    while len(queue) > 0:
        level_size = len(queue)
        current_level = []
        for i in range(level_size):
            current = queue.pop(0)
            
            if i == level_size - 1:
                result.append(current.val)
            
            current_level.append(current.val)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
    
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = right_view(root)
    
    print("Tree right view: ")
    for node in result:
        print(str(node) + " ", end='')
    print()
        
main()
                