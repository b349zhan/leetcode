from solution import longestCommonPrefix

def test_one():
    strs = ["flower","flow","flight"]
    assert longestCommonPrefix(strs) == "fl"

def test_two():
    strs = ["dog","racecar","car"]
    assert longestCommonPrefix(strs) == ""