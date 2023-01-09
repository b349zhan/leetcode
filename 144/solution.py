from typing import List, Optional
from ADTs.TreeNode import TreeNode
def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result = []
    stack = [root]
    while stack:
        node = stack.pop(-1)
        if node:
            stack.append(node.right)
            stack.append(node.left)
            result.append(node.val)
    return result