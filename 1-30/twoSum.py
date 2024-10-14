
def twoSum(nums, target):
    number_to_index = {}
    print('len', len(nums))
    for i in range(len(nums)):
        print('i', i)
        print(number_to_index[nums[i]])
        num_needed = target - nums[i]
        print('num_needed in number_to_index', num_needed in number_to_index)
        if num_needed in number_to_index:
            return [number_to_index[num_needed], i]
        
        number_to_index[nums[i]] = i
    return None

nums = [8, 8, 5, 5]
target = 10
print(twoSum(nums, target))
