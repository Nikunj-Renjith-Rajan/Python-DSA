# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None

def isSameTree(p, q):
        if p==None and q==None:
            return True
        if p==None or q==None or p.data!=q.data:
            return False
        return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)

root1=node(1)
root1.left=node(2)
root1.right=node(3)
root2=node(1)
root2.left=node(2)
root2.right=node(3)
print(isSameTree(root1,root2))
