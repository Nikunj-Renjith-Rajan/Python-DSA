# Given the root of a binary tree, invert the tree, and return its root.
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_list(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while queue and i < len(arr):
        curr = queue.popleft()
        # Left child
        if i < len(arr) and arr[i] is not None:
            curr.left = TreeNode(arr[i])
            queue.append(curr.left)
        i += 1
        # Right child
        if i < len(arr) and arr[i] is not None:
            curr.right = TreeNode(arr[i])
            queue.append(curr.right)
        i += 1
    return root

def invertTree(root):
        def invert(node):
            if node:
                invert(node.left)
                invert(node.right)
                node.left,node.right=node.right,node.left
            else:
                return
        invert(root)
        return root

def inorderTraversal(root):
        res=[]
        def inorder(node):
            if node:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)
            else:
                return
        inorder(root)
        return res

treelist = build_tree_from_list([1,2,3,4,5,None,8,None,None,6,7,9])
print("INORDER:",inorderTraversal(treelist))
print("INVERTED TREE (INORDER):",inorderTraversal(invertTree(treelist)))