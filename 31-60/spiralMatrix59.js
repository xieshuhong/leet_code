function spiralMatrix(n) {
    let matrix = Array.from({length: n}, () => Array(n).fill(0));
    let top = 0, bottom = n - 1, left = 0, right = n - 1, num = 1;

    while (left <= right) {
        for (let i = left; i <= right; i++) {
            matrix[top][i] = num ++;
        }
        top ++;
        for (let i = top; i <= bottom; i++) {
            matrix[i][right] = num ++;
        }
        right --;
        for (let i = right; i >= left; i--) {
            matrix[bottom][i] = num ++;
        }
        bottom --;
        for (let i = bottom; i >= top; i--) {
            matrix[i][left] = num ++;
        }
        left ++;
    }
    return matrix;
}

let lengthn = 3;
console.log('spiral matrix', spiralMatrix(lengthn));