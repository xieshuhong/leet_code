
function isBalanced(s) {

    let stack = [];
    const mapping = {')': '(', '}':'{', ']': '['};

    for (let letter of s) {
        if(letter in mapping) {
            let top_elements = stack.length > 0 ? stack.pop() : '#';
            if(mapping[letter] != top_elements) return false;
        } else {
            stack.push(letter);
        }

    }
    return stack.length == 0;
}

const balancedString = "{[()]}";
// const unbalancedString = "{[(])}";

console.log(`Is '${balancedString}' balanced?`, isBalanced(balancedString)); // true