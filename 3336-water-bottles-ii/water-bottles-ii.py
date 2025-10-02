class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            ans += 1
            numBottles -=(numExchange-1)
            numExchange += 1
        return ans