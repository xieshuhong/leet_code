function nQueens(n) {
    let col = new Set();
    let posDiag = new Set();
    let negDiag = new Set();

    let board = Array.from({length: n}, () => Array(n).fill('.'));
    let res = [];

    function backtracking(r) {

        console.log('starting a new row', r)
        if (r == n) {
           res = board.map(row => row.join(''));
           console.log('res', res)
        }
        

        for (let c = 0; c < n; c++) {
            console.log('True or False: ', col.has(c) || posDiag.has(r+c)||negDiag.has(r-c), 'c',c, 'col', col, 'r+c', r+c, 'posDiag', posDiag, 'r-c', r-c, 'negDiag', negDiag);
            if(col.has(c) || posDiag.has(r+c)||negDiag.has(r-c)) continue;

            col.add(c);
            posDiag.add(r+c);
            negDiag.add(r-c);
            board[r][c] = 'Q';

            console.log('row', r, 'column', c, 'posDiag', posDiag, 'negDiag', negDiag, 'board', board);

            backtracking(r+1);

            console.log('backing to the previous row', r);
            col.delete(c);
            posDiag.delete(r+c);
            negDiag.delete(r-c);
            board[r][c] = '.';
            console.log('row111', r, 'column111', c, 'posDiag111', posDiag, 'negDiag111', negDiag, 'board111', board);

        }
    }

    backtracking(0);
    return res;

}

console.log('nQueens', nQueens(4));