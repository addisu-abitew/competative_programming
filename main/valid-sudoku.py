class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # checked boxes
        for i in range(3):
            for j in range(3):
                if not self.isValidBox(board, i*3, j*3):
                    return False
        # check rows and columns
        for i in range(9):
            if not self.isValidCol(board, i) or not self.isValidRow(board, i):
                return False
        return True
        
    def isValidBox(self, board, init_row, init_col):
        checked = set()
        for row in range(init_row, init_row+3):
            for col in range(init_col, init_col+3):
                val = board[row][col]
                if val != '.' and val in checked:
                    return False
                checked.add(val)
        return True
    
    def isValidRow(self, board, row):
        checked = set()
        for col in range(9):
            val = board[row][col]
            if val != '.' and val in checked:
                return False
            checked.add(val)
        return True
    
    def isValidCol(self, board, col):
        checked = set()
        for row in range(9):
            val = board[row][col]
            if val != '.' and val in checked:
                return False
            checked.add(val)
        return True