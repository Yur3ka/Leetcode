class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        for i in range(n//2+1):
            if colors[0] != colors[n-1-i]:
                return n-1-i
            if colors[n-1] != colors[0+i]:
                return n-1-i
        return 0