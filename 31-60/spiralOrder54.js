function spiralOrder(matrix){
    if (!matrix.length) return [];

    let rows = matrix.length, cols = matrix[0].length;
    let top = 0, bottom = rows - 1, left = 0, right = cols - 1;
    let result = [];

    while(result.length < rows * cols) {
        if (left <= right) {
            for (let i = left; i <= right; i++) {
                result.push(matrix[top][i]);
            }
            top++;
        }
        if (top <= bottom) {
            for (let i = top; i <= bottom; i++) {
                result.push(matrix[i][right]);
            }
            right--;
        }
        if (top <= bottom) {
            for (let i = right; i >= left; i--) {
                result.push(matrix[bottom][i]);
            }
            bottom --;
        }
        if (left <= right) {
            for (let i = bottom; i >= top; i--) {
                result.push(matrix[i][left]);
            }
            left ++;
        }
    }
    return result;
}

const matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
];

console.log(spiralOrder(matrix));