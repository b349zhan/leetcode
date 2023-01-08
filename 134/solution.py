from typing import List
def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    temp = list(map(lambda i: gas[i]-cost[i], list(range(len(gas)))))
    if sum(temp)<0: return -1
    start = 0
    total = 0
    steps = 0
    while steps < len(gas)-1:
        end = (start + steps) % len(gas)
        total += temp[end]
        if total < 0:
            start = end+1
            end = start
            steps = 0
            total = 0
        else:
            steps += 1
    return start
