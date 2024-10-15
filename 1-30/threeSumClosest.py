

def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    
    print('nums', nums, 'closest_sum', closest_sum, '\n')
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        print('iiiiiiiiiiiiiiiiiiiiiiiiiiii', i, 'left', left, 'right', right, '\n')
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            print('nums[i]', nums[i], 'current_sum', current_sum, 'left', left,'nums[left]', nums[left], 'right', right, 'nums[right]', nums[right], '\n')
            print('current_sum', current_sum, 'current_sum - target', abs(current_sum - target), 'closest_sum - target', abs(closest_sum - target), '\n')
            if abs(current_sum - target) < abs(closest_sum - target):
                print('less than is true', closest_sum, '\n')
                closest_sum = current_sum
            print('closest_sum', closest_sum, '\n') 
            # ajust pointers based on the current sum
            if current_sum < target:   # increase the sum
                left += 1
            elif current_sum > target: # decrease the sum
                right -= 1
            else: # if the current sum is exactly the target, we return it immediately
                return current_sum
    return closest_sum


nums = [-1, 1, -4, 2]
target = 1

print(threeSumClosest(nums, target))