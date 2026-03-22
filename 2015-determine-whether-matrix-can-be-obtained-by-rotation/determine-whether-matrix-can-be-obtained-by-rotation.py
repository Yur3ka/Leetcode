class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rot(grid):
            rotated = list(zip(*grid[::-1]))
            rotated = [list(row) for row in rotated]
            return rotated
        for _ in range(4):
            mat = rot(mat)
            status = True
            for i in range(len(mat)):
                for j in range(len(mat)):
                    if mat[i][j] != target[i][j]:
                        status = False
                        break
            if status == True:
                return True
        return False
            