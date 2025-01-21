
def permute(nums, type) -> list:
    result = []
    print('resuluuuuuuuuuuu:', result)  
    print('type000000000000', type)
    # base case
    if (len(nums) == 1):
        print('len(nums) == 1----nums[:]: ', nums[:])
        return [nums[:]]
    
    print('calculate len for loop', len(nums))
    for i in range(len(nums)):
        print('iiiiiiiiiiiii', i)
        print('typeeeeeeeeeeeeeeee', type)
        n = nums.pop(0)
        print('pop n: ', n)
        perms = permute(nums, 1)
        print('back from base case--------------perms: ', perms, 'n', n, 'iiiiiiiiii', i)
        print('tttttttttttttttttttt', type)
        print('permsssssssssssssss: ', perms)
        
        print('resuliiiiiiiiiiiiii:', result)  
        for perm in perms:
            print('perm000: ', perm)
            print('n for perm in perms: ', n)
            perm.append(n)
            print('perm111: ', perm)
        result.extend(perms)
        print('result000: ', result)
        print('beffffffffffore nums: ', nums)
        nums.append(n)
        print('afttttttttttter nums: ', nums)
    print('result111: ', result)      
    return result


nums = [1, 2, 3]
print(permute(nums, 0))