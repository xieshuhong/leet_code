
def solveNQueens(n) -> list:
    col = set()
    posDiag = set()
    negDiag = set()

    res = []
    board = [["."] * n for _ in range(n)]
    print('board', board)

    def backtrack(r):
        print('r from the start of the backtrack', r)
        if r == n:
            copy = ["".join(row) for row in board]
            print('copy', copy)
            res.append(copy)
            return
        
        for c in range(n):
            print('c', c)
            print('ccccccccccccc', c, 'col', col,'r', r, 'r+c', r+c, 'posDiag', posDiag, 'r', r, 'r-c', r-c, 'negDiag', negDiag)
            print('true or false', c in col or (r+c) in posDiag or (r-c) in negDiag)
            if c in col or (r+c) in posDiag or (r-c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            board[r][c] = "Q"
            print('colllllllllllllllllll', col, 'r', r, 'c', c, '[r][c]', board[r][c], 'board', board, 'posDiag', posDiag, 'negDiag', negDiag, 'Start backtrack...')
            backtrack( r + 1)

            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c] = "."
            print('rrrrrrrrrrrrrrafter remove:', board)
            
    backtrack(0)
    return res



print(solveNQueens(4))