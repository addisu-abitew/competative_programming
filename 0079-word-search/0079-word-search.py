class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row, col, path):
            if len(path) == len(word): return True
            
            if ((row+1, col) not in path) and (row+1<rows) and (board[row+1][col] == word[len(path)]):
                row += 1
                path.add((row, col))
                if backtrack(row, col, path): return True
                path.remove((row,col))
                row -= 1
            if ((row, col+1) not in path) and (col+1<cols) and (board[row][col+1] == word[len(path)]):
                col += 1
                path.add((row, col))
                if backtrack(row, col, path): return True
                path.remove((row,col))
                col -= 1
            if ((row-1, col) not in path) and (row>0) and (board[row-1][col] == word[len(path)]):
                row -= 1
                path.add((row, col))
                if backtrack(row, col, path): return True
                path.remove((row,col))
                row += 1
            if ((row, col-1) not in path) and (col>0) and (board[row][col-1] == word[len(path)]):
                col -= 1
                path.add((row, col))
                if backtrack(row, col, path): return True
                path.remove((row,col))
            
            return False
        rows, cols = len(board), len(board[0])
        row = col = 0
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if backtrack(row, col, set({(row, col)})): return True
        return False