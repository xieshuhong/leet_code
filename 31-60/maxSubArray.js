
function maxSubArray(nums) {
    let max_value = -Infinity;
    let current_value = 0;

    for (let num of nums) {
        current_value = Math.max(num, current_value + num);
        max_value = Math.max(max_value, current_value);
    }
    return max_value;
}

const nums = [-2,1,-3,4,-1,2,1,-5,4];
console.log(maxSubArray(nums));
