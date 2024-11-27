from collections import defaultdict
from typing import List

def groupAnagrams(strs) -> list:
    # this is a dictionary for key and value to store to it
    # It's gonna be look like this: {(1, 0, ..., 1): ["eat", "tea", "ate"]}
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s)

    return res.values()


strs=["eat","tea","tan","ate","nat","bat"]

groupAnagrams(strs)