class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maxFre = 0
        c = Counter(nums)
        ans = 0
        for k,v in c.items():
            if v > maxFre:
                maxFre = v
                ans = v
            elif v == maxFre:
                ans += v
        return ans