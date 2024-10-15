
def twoSum(nums, target):
    number_to_index = {}
    print('len', len(nums))
    for i in range(len(nums)):
        print('i', i, 'nums[i]', nums[i])
        num_needed = target - nums[i]
        print('num_needed in number_to_index', num_needed in number_to_index, 'number_to_index', number_to_index, num_needed)
        if num_needed in number_to_index:
            return [number_to_index[num_needed], i]
        
        number_to_index[nums[i]] = i
    return None

nums = [8, 8, 5, 6]
target = 11
print(twoSum(nums, target))
