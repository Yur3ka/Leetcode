class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flatt = []
        for row in grid:
            for num in row:
                flatt.append(num)
        flatt.sort()
        mid = flatt[len(flatt)//2]
        ans = 0
        for num in flatt:
            if (mid - num) % x != 0:
                return -1
            ans += abs(mid-num)//x
        return ans