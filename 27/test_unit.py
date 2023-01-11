from solution import removeElement
def test_one():
    nums = [3, 2, 2, 3]
    val = 3
    assert removeElement(nums, val) == 2
    assert nums[:2]==[2,2]

def test_two():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    assert removeElement(nums, val) == 5
    assert sorted(nums[:5])==[0, 0, 1, 3, 4]
    