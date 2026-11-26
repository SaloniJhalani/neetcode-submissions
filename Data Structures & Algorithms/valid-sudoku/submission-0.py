class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(0,9):
            temp = [board[row][col] for col in range(0,9) if board[row][col] != "."]
            if len(set(temp)) != len(temp):
                return False
        
        for col in range(0,9):
            temp = [board[row][col] for row in range(0,9) if board[row][col] != "."]
            if len(set(temp)) != len(temp):
                return False

        for box_row in range(0, 9, 3):          # top-left row of each box: 0, 3, 6
            for box_col in range(0, 9, 3):      # top-left column of each box: 0, 3, 6
                temp = [board[box_row + r][box_col + c]
                        for r in range(3) for c in range(3)
                        if board[box_row + r][box_col + c] != "."]
                if len(set(temp)) != len(temp):
                    return False

        return True

        