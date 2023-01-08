from typing import List
def maxIceCream(costs: List[int], coins: int) -> int:
    # List
    # Time O(nlog(n))
    # Space O(1)
    costs.sort()
    total = 0
    soFar = 0
    for i in range(len(costs)):
        if costs[i] + soFar <= coins:
            total += 1
            soFar += costs[i]
        else:
            break
    return total