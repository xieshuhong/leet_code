
#Given a string s and a dictionary of strings wordDict, 
#return true if s can be segmented into a space-separated sequence of one or more dictionary words.

def wordBreak(s: str, wordDict: list[str]) -> bool:
    word_set = set(wordDict)  # Use a set for fast lookup
    dp = [False] * (len(s) + 1)
    dp[0] = True  # Base case: empty string
    
    print(dp)
    
    for i in range(1, len(s) + 1):
        print('i', i)
        for j in range(i):
            print('j', j, 'dp[j]', dp[j], 'i', i, 's[j:i]', s[j:i])
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  # No need to check further if true
    
    return dp[len(s)]



s = "leetcode"
wordDict = ["leet", "code"]
print(wordBreak(s, wordDict))
