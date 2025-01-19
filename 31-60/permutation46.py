
def permute(nums) -> list:
    result = []
    
    # base case
    if (len(nums) == 1):
        print('len(nums) == 1----nums[:]: ', nums[:])
        return [nums[:]]
    
    print('lennnnnnnnnnn', len(nums))
    for i in range(len(nums)):
        print('len(nums)', len(nums))
        print('iiiiiiiiiiiii', i)
        n = nums.pop(0)
        print('pop n: ', n)
        perms = permute(nums)
        print('back from base case--------------perms: ', perms, 'n', n, 'iiiiiiiiii', i)
        
        for perm in perms:
            print('perm000: ', perm)
            print('n for perm in perms: ', n)
            perm.append(n)
            print('perm111: ', perm)
        result.extend(perms)
        print('result000: ', result)
        print('before nums: ', nums)
        nums.append(n)
        print('after nums: ', nums)
    print('result111: ', result)      
    return result


nums = [1, 2, 3]
print(permute(nums))