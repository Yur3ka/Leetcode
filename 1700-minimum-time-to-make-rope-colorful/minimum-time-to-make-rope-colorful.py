class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        need = 0
        total = neededTime[0]
        curr = neededTime[0]
        for i in range(1,len(colors)):
            total += neededTime[i]
            if colors[i] == colors[i-1]:
                curr = max(curr,neededTime[i])
            else:
                need += curr
                curr = neededTime[i]
        need += curr
        return total - need