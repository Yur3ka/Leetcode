class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[False]*10 for _ in range(9)]
        cols = [[False]*10 for _ in range(9)]
        boxes = [[False]*10 for _ in range(9)]
        
        empty_cells = []

        # khởi tạo
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    rows[i][int(num)] = True
                    cols[j][int(num)] = True
                    boxes[(i//3)*3 + j//3][int(num)] = True
                else:
                    empty_cells.append((i, j))

        def backtrack(idx):
            if idx == len(empty_cells):
                return True
            i, j = empty_cells[idx]
            b = (i//3)*3 + j//3
            for num in range(1, 10):
                if not rows[i][num] and not cols[j][num] and not boxes[b][num]:
                    # đặt số
                    board[i][j] = str(num)
                    rows[i][num] = cols[j][num] = boxes[b][num] = True

                    if backtrack(idx + 1):
                        return True

                    # backtrack
                    board[i][j] = '.'
                    rows[i][num] = cols[j][num] = boxes[b][num] = False
            return False

        backtrack(0)