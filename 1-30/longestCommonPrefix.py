# 14
def longestCommonPrefix(strs):
    # If the input list is empty, return an empty string
    if not strs:
        return ""
    # Find the shortest string in the list
    min_str = min(strs, key=len)
    
    
    print('min_str', min_str)
    
    # Iterate over the characters in the shortest string
    for i in range(len(min_str)):
        # Compare the character at position i in all strings
        for string in strs:
            print('string[i] != min_str[i]',string, string[i], min_str, min_str[i])
            print('string[i] != min_str[i]',string[i] != min_str[i])
            if string[i] != min_str[i]:
                # If mismatch found. It takes the substring of min_str from the beginning up to index i
                print('min_str', min_str[:i])
                return min_str[:i] 
    
    # If no mismatches, the entire shortest string is the common prefix
    return min_str



s = ["flower", "flow", "flight"]
print(longestCommonPrefix(s))