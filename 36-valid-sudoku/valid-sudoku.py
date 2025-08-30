class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(x,y, board):
            for i in range(9):
                if board[x][y] == board[x][i] and y != i:
                    return False
            return True
        def checkCol(x,y,board):
            for i in range(9):
                if board[x][y] == board[i][y] and x!=i:
                    return False
            return True

        def checkSquare(x,y,board):
            vert = x //3
            horz = y //3
            for i in range(vert*3, vert*3+3):
                for k in range(horz*3, horz*3+3):
                    if board[x][y] == board[i][k] and (x !=i or y!=k):
                        return False
            return True
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if not (checkRow(i,j,board) and checkCol(i,j,board) and checkSquare(i,j,board)):
                    return False
        return True