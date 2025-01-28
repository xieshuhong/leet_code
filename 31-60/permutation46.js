function permute(nums) {
    const result = [];

    if (nums.length === 1) {
        return [nums.slice()];
    }

    for (let i = 0; i < nums.length; i++) {
        const n = nums.shift();

        const perms = permute(nums);
        
        for (const perm of perms) {
            perm.push(n);
        }
        result.push(...perms);
        nums.push(n);
    }
    return result;
}

const nums = [1, 2, 3];
permute(nums);