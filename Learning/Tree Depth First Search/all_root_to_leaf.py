from has_path import TreeNode

def all_root_to_leaf(root):
    all_paths = []
    find_all_paths(root, all_paths)
    return all_paths

def find_all_paths(root, all_paths, current_path=[]):
    if not root:
        return
    
    current_path.append(root.val)
    
    if root.left is None and root.right is None:
        all_paths.append(list(current_path))
    
    find_all_paths(root.left, all_paths, current_path)
    find_all_paths(root.right, all_paths, current_path)
    
    del current_path[-1]
    
    
def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print("Tree has path: %s" % str(all_root_to_leaf(root)))
 
main()