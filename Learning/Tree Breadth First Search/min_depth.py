class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

def find_min_depth(root):
    queue = [root]
    level = 0
    
    while len(queue) > 0:
        level_size = len(queue)
        current_level = []
        
        level += 1
        
        for _ in range(level_size):
            current = queue.pop(0)
            
            current_level.append(current.val)
            
            if not current.left and not current.right:
                return level
            else:
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
    
    return level

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(11)
    
    print("minimum depth: " + str(find_min_depth(root)))
    
main()