
def maxArea(heights) -> int:
    
    res = 0
    l, r = 0, len(heights) - 1

    while l < r :
        area = (r - l) * min(heights[l], heights[r])
        res = max(res, area)
        
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return res


heights = [1,8,6,2,5,4,8,3,7]

print(maxArea(heights)) 