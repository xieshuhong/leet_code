
def spiralOrder(matrix) -> list:
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows-1, 0, cols-1
        print('rows', len(matrix), 'cols', len(matrix[0]))
        print('top', top, 'bottom', bottom, 'left', left, 'right', right)
        result = []
        
        
        while len(result) < rows * cols:
            print('true or false', len(result) < rows * cols)
            print('left <= right11', left <= right)
            if left <= right:
                for i in range(left, right+1):
                    print('top, i', top, i, 'left', left, 'right', right)
                    result.append(matrix[top][i])
                    print('left and right', result)
                top += 1
                print('top', top)

            print('top <= bottom11', top <= bottom)
            if top <= bottom:
                for i in range(top, bottom+1):
                    print('i,right', i, right, 'from top', top, 'from bottom', bottom)
                    result.append(matrix[i][right])
                    print('top and bottom', result)
                right -= 1
                print('right', right)
            
            print('top <= bottom22', top <= bottom)
            if top <= bottom:
                for i in range(right, left-1, -1):
                    print('bottom, i', bottom, i, 'right', right, 'left-1', left - 1)
                    result.append(matrix[bottom][i])
                    print('right and left - 1', result)
                bottom -= 1
                print('bottom', bottom)

            print('left <= right', left <= right)
            if left <= right:
                for i in range(bottom, top-1, -1):
                    print('i, left', i, left, 'bottom', bottom, 'top-1', top-1)
                    result.append(matrix[i][left])
                    print('bottom and top - 1', result)
                left += 1
                print('left', left)
        
        return result


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))

