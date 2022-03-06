from has_path import TreeNode

def sum_of_paths(root):
    return find_all_paths(root, 0)
    

def find_all_paths(root, sum):
    if not root:
        return 0
    
    sum = 10 * sum + root.val
    
    if root.left is None and root.right is None:
        return sum
    
    return find_all_paths(root.left, sum) + find_all_paths(root.right, sum)
    

def main():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)

    print("Tree has path: " + str(sum_of_paths(root)))
 
main()