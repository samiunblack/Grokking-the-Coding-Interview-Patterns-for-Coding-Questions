from has_path import TreeNode

def all_paths(root, sum):
    all_path = []
    find_path_recursively(root, sum, [], all_path)
    return all_path

def find_path_recursively(root, sum, current_path, all_path):
    if root is None:
        return 
    
    current_path.append(root.val)
    
    if root.val == sum and root.left is None and root.right is None:
        all_path.append(list(current_path))
    
    else:
        find_path_recursively(root.left, sum - root.val, current_path, all_path)
        find_path_recursively(root.right, sum - root.val, current_path, all_path)
        
    del current_path[-1]

def main():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(7)

    print(all_paths(root, 12))

main() 