from solution import preorderTraversal
from ADTs.TreeNode import TreeNode
def test_one():
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert preorderTraversal(root)==[1,2,3]
def test_two():
    root = None
    assert preorderTraversal(root)==[]