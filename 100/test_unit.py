from solution import isSameTree
from ADTs.TreeNode import TreeNode
def test_one():
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert isSameTree(p, q)==True

def test_two():
    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))
    assert isSameTree(p, q)==False

def test_three():
    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(1), TreeNode(2))
    assert isSameTree(p, q)==False