
def canJump(nums) -> bool:
    goal = len(nums) -1
    print('goal', goal)

    # starting from the last index to the begining index
    for i in range(len(nums)-2, -1, -1): 
        print('i', i, 'nums[i]', nums[i])
        if i + nums[i] >= goal:
            goal = i
            print('goal111', goal)
            
    return True if goal == 0 else False


nums = [2,3,1,1,4]
nums1 = [3,2,1,0,4]
    
print(canJump(nums1))