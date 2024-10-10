// leetcode 14
function longestCommonPrefix(strs) {
    // If the input array is empty, return an empty string
    if (strs.length === 0) return "";

    // Find the shortest string in the array
    let minStr = strs.reduce((a, b) => a.length <= b.length ? a : b);

    // Iterate over each character of the shortest string
    for (let i = 0; i < minStr.length; i++) {
        // Compare the character at position i in each string
        for (let str of strs) {
            if (str[i] !== minStr[i]) return minStr.slice(0, i);
        }
    }
    return minStr;
}

strs = ["flow", "flowers", "flood"]
console.log(longestCommonPrefix(strs))