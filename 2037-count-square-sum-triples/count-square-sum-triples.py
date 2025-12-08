class Solution:
    def countTriples(self, n: int) -> int:
        # square = set()
        sq = [0]
        ans = 0
        for i in range(1,n+1):
            sq.append(i*i)
        square = set(sq)
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if (sq[i]+sq[j]) in square:
                    ans += 2
        return ans
