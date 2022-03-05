class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def has_path(root, s):
    if root == None:
        return False

    if root.val == s and root.left is None and root.right is None:
        return True
    
    return has_path(root.left, s - root.val) or \
        has_path(root.right, s - root.val)

    
def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    
    print("Tree root has path: " + str(has_path(root, 23)))
    
main()