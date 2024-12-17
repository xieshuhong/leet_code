import java.util.*;
public class SolveNQueens {

     public List<List<String>> solveNQueens(int n) {
        Set<Integer> col = new HashSet<>();
        Set<Integer> posDiag = new HashSet<>();
        Set<Integer> negDiag = new HashSet<>();
        List<List<String>> res = new ArrayList<>();
        
        char[][] board = new char[n][n];
        for (char[] row: board) {
            Arrays.fill(row, '.');
        }
        backtrack(0, n, board, col, posDiag, negDiag, res);
        return res;
     }

     private void backtrack(int r, int n, char[][] board, Set<Integer> col, Set<Integer> posDiag, Set<Integer> negDiag, List<List<String>> res) {
        if (r == n) {
            List<String> copy = new ArrayList<>();
            for (char[] row: board) {
                System.out.println(row);
                copy.add(new String(row));
            }
            System.out.println("coping: " + copy);
            res.add(copy);
            System.out.println("res: " +  res);
            return;
        }
        for (int c = 0; c < n; c++) {
            if (col.contains(c) || posDiag.contains(r + c) || negDiag.contains(r - c)) {
                continue;
            }
            col.add(c);
            posDiag.add(r+c);
            negDiag.add(r-c);
            board[r][c] = 'Q';

            backtrack(r + 1, n, board, col, posDiag, negDiag, res);
            col.remove(c);
            posDiag.remove(r+c);
            negDiag.remove(r-c);
            board[r][c] = '.';
        }
     }


     public static void main(String[] args) {
        SolveNQueens solver = new SolveNQueens();
        int n = 4; 
        List<List<String>> solutions = solver.solveNQueens(n);

        System.out.println("solutions: " +solutions);

     }
}