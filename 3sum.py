# 3Sum
# i != j, i != k, and j != k
# nums[i] + nums[j] + nums[k] == 0

#. 1. Sort the array nums.
#. 2. For each element in the sorted array:
#  3. - Skip duplicates.
#   - Set left pointer to i+1, right pointer to the end of the array.
#   - While left < right:
#     - Calculate the sum of nums[i], nums[left], and nums[right].
#     - If the sum is zero, add the triplet to the result.
#     - If the sum is less than zero, move the left pointer to the right.
#     - If the sum is greater than zero, move the right pointer to the left.
#     - Skip duplicates for left and right pointers.
#  4. Return the result list.


def threeSum(nums):

    #. 1. Sort the array nums.
    nums.sort()
    res = []
    
    # Step 2: Iterate over the array, treating each number as the first element
    for i in range(len(nums)):
         # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums [i - 1]:
            continue
        
        # Step 3: Two-pointer technique for the remaining part of the array
        left, right = i + 1, len(nums) - 1
        while left < right:
            total  = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                
                # Move left and right to the next different numbers & Skip duplicate
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
                
            elif total < 0:
                 left += 1   # We need a larger sum
            else:
                 right -= 1 # We need a smaller sum
                 
    return res


arr = [-1, 0, 1, 2, -1, -4]
newarr = threeSum(arr)
print(newarr)


            
            