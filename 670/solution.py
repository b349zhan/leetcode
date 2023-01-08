from collections import deque
def maximumSwap(num: int) -> int:
    # Hashmap
    # Time O(log(n))
    # Space O(log(n))
    data = {}
    source = list(str(num))
    for idx, item in enumerate(source):
        if item not in data: data[item] = deque([idx])
        else: data[item].append(idx)
    for idx, item in enumerate(source):
        max_key = max(data.keys())
        if item < max_key:
            right_index = data[max_key][-1]
            temp = source[idx]
            source[idx]=max_key
            source[right_index] = temp
            return int("".join(source))
        else:
            data[max_key].popleft()
            if not data[max_key]: del data[max_key]
    return num
