from typing import List
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # Hashmap
    # Time O(nm), where m is the longest string's length
    # Space O(nm), where m is the longest string's length
    def get_tuple(s):
        res = [0]*26
        for i in range(len(s)):
            res[ord(s[i])-ord('a')] += 1
        return tuple(res)
    d = {}
    for item in strs:
        current = get_tuple(item)
        if current not in d: d[current] = [item]
        else: d[current].append(item)
    return list(d.values())
