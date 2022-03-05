class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right


def zigzag_traversal(root):
    queue = [root]
    result = [] 
    left_to_right = True
    
    while queue != []:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            current = queue.pop(0)
            
            if left_to_right:
                current_level.append(current.val)
            else:
                current_level.insert(0, current.val)

            if current.left:
                    queue.append(current.left)
            if current.right:
                queue.append(current.right)
            
        
        result.append(current_level)
        left_to_right = not left_to_right
    
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    
    zigzag_traversal(root)
    print("Level order traversal: " + str(zigzag_traversal(root)))
    
main()