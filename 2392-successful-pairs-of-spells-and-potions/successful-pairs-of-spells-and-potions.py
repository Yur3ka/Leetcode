class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        m = len(potions)
        potions.sort()
        for i in range(len(spells)):
            atLeast = ceil(success/spells[i])
            n = bisect_left(potions,atLeast)
            ans.append(m-n)
        return ans