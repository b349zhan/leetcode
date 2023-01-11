from typing import Optional, List
from ADTs.TreeNode import TreeNode

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode])-> bool:
    # Tree
    # Time O(n)
    # Space O(n)
    if not p and not q: return True
    if not p or not q: return False
    if p.val != q.val: return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)