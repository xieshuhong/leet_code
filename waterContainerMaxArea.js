
function maxArea(heights) {
    let maxArea = 0;
    let l = 0, r = heights.length - 1;

    while (l < r) {
        let area = Math.min(heights[r], heights[l]) * (r - l);
        maxArea = Math.max(maxArea, area);
        if (heights[r] > heights [l]) l += 1
        else r -= 1
    }
    return maxArea;
}

const heights = [1,8,6,2,5,4,8,3,7];
console.log(maxArea(heights));