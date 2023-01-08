from typing import List
def longestCommonPrefix(strs: List[str]) -> str:
    # Greedy algorithm
    # Time O(nm), where m is the maximum length of the string in the list
    # Space O(m), where m is the maximum length of the string in the list

    if len(strs)==0: return ""
    if len(strs)==1: return strs[0]
    prefix=strs[0]
    for i in range(1,len(strs)):
        new_str = strs[i]
        j = 0
        while j < min(len(prefix), len(new_str)):
            if prefix[j]==new_str[j]:
                j += 1
            else: break
        prefix = prefix[:j]
    return prefix