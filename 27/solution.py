from typing import List
def removeElement(nums: List[int], val: int)->int:
    # Array
    # Time O(n)
    # Space O(1)
    start = 0
    firstValidIndex = 0
    while start < len(nums):
        if nums[start]==val:
            print(f"Hit at {start}, firstValidIndex:{firstValidIndex}")
            while firstValidIndex < len(nums) and nums[firstValidIndex] == val:
                firstValidIndex += 1
            if firstValidIndex == len(nums): break
            temp = nums[start]
            nums[start]=nums[firstValidIndex]
            nums[firstValidIndex] = temp
        else:
            firstValidIndex += 1
        start += 1
    return start