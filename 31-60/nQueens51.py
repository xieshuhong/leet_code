
def solveNQueens(n) -> list:
    col = set()
    posDiag = set()
    negDiag = set()

    res = []
    board = [["."] * n for i in range(n)]
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
            if c in col or (r+c) in posDiag or (r-c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            board[r][c] = "Q"
            print('col', col, 'posDiag', posDiag, 'negDiag', negDiag)
            backtrack( r + 1)

            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c] = "."
            
    backtrack(0)
    return res



solveNQueens(4)