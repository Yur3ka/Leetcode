class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x < y:
            return self.hammingDistance(y,x)
        elif x == y:
            return 0
        else:
            ans = 0
            while x:
                if 1&x != 1&y:
                    ans += 1
                x //=2
                y//=2
            return ans