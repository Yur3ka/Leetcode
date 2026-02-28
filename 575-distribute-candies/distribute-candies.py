class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        ans = 0
        s = len(candyType)
        maxCandies = s // 2
        maxType = len(set(candyType))
        for i in range(len(candyType)):
            if ans < maxCandies and ans < maxType:
                ans += 1
            else:
                break
        return ans