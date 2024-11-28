
function groupAnagram49(str) {
    let res = {}
    for (let s of str) {
        let zeros = Array(26).fill(0);
        for (let c of s) zeros[c.charCodeAt(0) - 'a'.charCodeAt(0)] +=1;

        let key = zeros.join(',')
        if (!res[key]) res[key] = []
        res[key].push(s);
    }
    return Object.values(res);
}

let strs=["eat","tea","tan","ate","nat","bat"]

console.log(groupAnagram49(strs))