

function twoSum(nums, target) {
    const numberToIndex = {}
    for (let i = 0; i <= nums.length; i++) {
        const numberNeeded = target - nums[i];
        if (numberToIndex[numberNeeded] !== undefined) {
            return [numberToIndex[numberNeeded], i]
        }
        numberToIndex[nums[i]] = i;
    }
}


let nums = [5, 5], target = 10
console.log(twoSum(nums, target))