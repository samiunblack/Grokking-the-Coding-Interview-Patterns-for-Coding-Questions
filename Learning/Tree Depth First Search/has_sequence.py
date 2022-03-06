from has_path import TreeNode

def has_sequence(root, sequence):
    if not root:
        return len(sequence) == 0
    return find_path_recursive(root, sequence, 0)

def find_path_recursive(root, sequence, index):
    if root is None:
        return False

    seq_len = len(sequence)
    
    if index >= seq_len or root.val != sequence[index]:
        return False

    if root.left is None and root.right is None and index == seq_len - 1:
        return True

    return find_path_recursive(root.left, sequence, index + 1) or \
        find_path_recursive(root.right, sequence, index + 1)
    

def main():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)

    print("Tree has path: %s" % str(has_sequence(root, [1, 9, 9])))
 
main()