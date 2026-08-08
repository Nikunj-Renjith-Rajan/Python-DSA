# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

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

def rootleafsum(root):
    def dfs(node,curr_sum):
        if not node:
            return 0
        curr_sum=curr_sum*10+node.val

        if not node.left and not node.right:
            return curr_sum

        return dfs(node.left,curr_sum)+dfs(node.right,curr_sum)
    return dfs(root,0)

treelist = build_tree_from_list([1,2,3,4,5,None,8,None,None,6,7,9])
print(rootleafsum(treelist))