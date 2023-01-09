from typing import List
def generate(numRows: int) -> List[List[int]]:
    # Array
    # Time O(n^2)
    # Space O(n^2)
    result = [[1]]
    if numRows == 1: return result
    result.append([1, 1])
    if numRows == 2: return result 
    current = 2
    while current < numRows:
        temp_result = [1]
        start = 0
        while start < len(result[-1])-1:
            temp_result.append(result[-1][start]+result[-1][start+1])
            start += 1
        temp_result.append(1)
        result.append(temp_result)
        current += 1
    return result
