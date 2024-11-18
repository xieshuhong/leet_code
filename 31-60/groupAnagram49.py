from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # using a defaultdict to group words by their character counts
    res = defaultdict(list)
    
    print('res', res)
    
    for s in strs:
        # Create a count of 26 zeros (for a to z)
        count = [0] * 26
        print('count', count)
        # Count each character's frequency in the string
        for c in s:
            count[ord[c] - ord['a']] += 1
            print("ord[c] - ord['a']", ord[c] - ord['a'])
        # Use the tuple of counts as a key to group anagrams
        res[tuple(count)].append(s)
        print("tuple(count)", tuple(count))
        
    # Return the grouped anagram
    print('res.values', res.values)
    return list(res.values)


strs=["eat","tea","tan","ate","nat","bat"]

groupAnagrams(strs)