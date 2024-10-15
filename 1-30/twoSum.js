

function twoSum(nums, target) {
    const numberToIndex = {}
    for (let i = 0; i <= nums.length; i++) {
        const numberNeeded = target - nums[i];
        if (numberNeeded in numberToIndex) { // numberToIndex[numberNeeded] !== undefined also works!
            return [numberToIndex[numberNeeded], i]
        }
        numberToIndex[nums[i]] = i;
    }
    return null
}


let nums = [7, 5, 9, 6], target = 15
console.log(twoSum(nums, target))