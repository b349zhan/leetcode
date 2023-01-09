from solution import groupAnagrams
def test_one():
    strs=["eat","tea","tan","ate","nat","bat"]
    result = groupAnagrams(strs)
    actual =  [["bat"],["nat","tan"],["ate","eat","tea"]]
    result_dict = {}
    actual_dict = {}
    for item in result:
        result_dict["".join(sorted(item[0]))]=set(item)
    for item in actual:
        actual_dict["".join(sorted(item[0]))]=set(item)
    print(actual_dict, result_dict)
    assert actual_dict==result_dict
def test_two():
    strs=[""]
    assert groupAnagrams(strs)==[[""]]