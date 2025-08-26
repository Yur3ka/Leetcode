class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = 0
        max_area = 0
        for i,j in dimensions:
            diag = i*i + j*j
            if diag > max_diag:
                max_diag = diag
                max_area = i*j
            elif diag == max_diag:
                max_area = max(i*j,max_area)
        return max_area