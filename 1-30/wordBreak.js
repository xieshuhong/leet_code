function wordBreak(s, wordDict) {
    const dp = Array(s.length + 1).fill(false);
    dp[0] = true;

    for (let i = 1; i <= s.length; i++) {
        for (let j = 0; j < i; j++) {
            console.log('j', j,'i', i, s.substring(j, i))
            if([j] && wordDict.find((element) => element == s.substring(j, i))) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[s.length];
}

const s = "leetcode";
const wordDict = ["leet", "code"];

console.log(wordBreak(s, wordDict));  // Output: true